import logging
import os
import shutil
import sys
import tarfile

import requests

from . import config, database, paths


def download_file(url: str) -> str:
    """Download a file to a temporary folder

    Args:
        url: Link to the file to be downloaded

    Returns:
        Path to the downloaded file
    """
    ITER_CHUNK_SIZE = 100*1024

    # prepare download folder
    download_folder = paths.get_tmp_download_dir().joinpath('g4dsdw_download')
    os.makedirs(download_folder, exist_ok=True)
    download_file_path = download_folder.joinpath(os.path.basename(url))
    logging.debug(f'Writing download to {download_file_path}')

    # send request
    response = requests.get(url, allow_redirects=True, stream=True)
    if not response.ok:
        raise Exception(f'Failed to fetch {url}')

    # get download size for progress bar
    download_size = 0
    total_size = int(response.headers.get('content-length'))
    logging.info(f'Download size: {total_size*1e-6:.1f} MB')

    # open new file
    with open(download_file_path, 'wb') as download_file:
        # download in chunks
        for chunk in response.iter_content(chunk_size=ITER_CHUNK_SIZE):
            download_file.write(chunk)

            # update progress bar
            download_size += len(chunk)
            downloaded_perc_n50 = int(50 * download_size / total_size)
            sys.stdout.write('\r['+('='*downloaded_perc_n50)+(' '*(50 - downloaded_perc_n50))+f'] ({download_size*1e-6:.1f} / {total_size*1e-6:.1f})')
            sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()

    return download_file_path


def install_dataset(dataset: str, version: str, manual: bool) -> None:
    """Install a dataset

    Args:
        dataset: Name of the dataset to install
        version: Version of the dataset to install
        manual: Mark dataset as manually installed
    """
    config_ = config.Config()
    # check if dataset exists
    logging.debug(f'Checking for dataset {dataset} version {version}')
    if not dataset in database.datasets:
        raise Exception(f'Dataset {dataset} is not in database, please run `g4dsdw list ds` for supported datasets')
    if not version in database.datasets[dataset]['versions']:
        raise Exception(f'Version {version} of dataset {dataset} is not in database, please run `g4dsdw list {dataset}` for supported version')
    # check if already installed
    if config_.is_dataset_installed(dataset, version):
        logging.info(f'Dataset {dataset} version {version}, skipping download')
        if manual:
            logging.info(f'Setting dataset {dataset} version {version} as manually installed')
            config_.set_dataset_installed(dataset, version, True)
        return
    # get destination folder
    dest = paths.get_default_install_dest()
    os.makedirs(dest, exist_ok=True)
    # TODO check if writable
    # download dataset
    logging.info(f'Downloading dataset {dataset} version {version}')
    url = database.datasets[dataset]['versions'][version]
    logging.debug(f'Download URL dataset from {url}')
    out_file_path = download_file(url)
    # extract to destination folder
    logging.debug(f'Extracting {os.path.basename(out_file_path)}')
    with tarfile.open(out_file_path, 'r:*') as out_file:
        out_file.extractall(dest)
    # mark as installed
    config_.set_dataset_installed(dataset, version, manual)
    logging.info(f'Successfully installed dataset {dataset} version {version}')


def uninstall_dataset(dataset: str, version: str) -> None:
    """Uninstall a dataset
    """
    config_ = config.Config()
    # check if dataset is marked as installed
    logging.debug(f'Checking if dataset {dataset} version {version} is installed')
    if not config_.is_dataset_installed(dataset, version):
        raise Exception(f'Dataset {dataset} version {version} is not installed')
    # get destination folder
    dest = paths.get_default_install_dest()
    dataset_dest = dest.joinpath(f'{dataset}{version}')
    # remove file tree
    shutil.rmtree(dataset_dest)
    # mark as uninstalled
    config_.set_dataset_uninstalled(dataset, version)
    logging.info(f'Successfully uninstalled dataset {dataset} version {version}')


def install_g4(version: str) -> None:
    """Install datasets for a Geant4 version

    Args:
        version: Geant4 version for which to install datasets
    """
    config_ = config.Config()
    # check if version exist
    logging.debug(f'Checking for Geant4 version {version}')
    if not version in database.geant4_versions:
        raise Exception(f'Geant4 version {version} is not in database, please run `g4dsdw list g4` for supported versions')
    # mark g4 version as installed in config
    config_.set_g4_installed(version)
    # get resolved Geant4 version
    resolved_version = database.resolve_g4_link(version)
    logging.debug(f'Using database entry of Geant4 version {resolved_version}')
    # download datasets
    logging.info(f'Downloading datasets for Geant4 version {version}')
    for dataset, dataset_version in database.geant4_versions[resolved_version].items():
        install_dataset(dataset, dataset_version, False)


def uninstall_g4(version: str) -> None:
    """Uninstall automatically installed datasets for a Geant4 version

    Args:
        version: Geant4 version for which to uninstall datasets
    """
    config_ = config.Config()
    # check if version installed
    logging.debug(f'Checking if datasets for Geant4 version {version} are installed')
    if not config_.is_g4_installed(version):
        raise Exception(f'Geant4 version {version} is not installed')
    # mark g4 version as uninstalled in config
    config_.set_g4_uninstalled(version)
    # get resolved Geant4 version
    resolved_version = database.resolve_g4_link(version)
    logging.debug(f'Using database entry of Geant4 version {resolved_version}')
    # check for automatically downloaded dataset versions
    datasets_to_check = database.geant4_versions[resolved_version]
    for dataset, dataset_version in datasets_to_check.items():
        is_manual = config_.is_dataset_manual(dataset, dataset_version)
        if is_manual is None:
            logging.info(f'Skipping uninstalling {dataset} version {version} since it is not installed')
            continue
        if is_manual:
            logging.info(f'Skipping uninstalling {dataset} version {version} since it was manually installed')
        else:
            uninstall_dataset(dataset, version)
