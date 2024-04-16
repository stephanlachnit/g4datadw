import pathlib

def get_default_install_dest() -> pathlib.Path:
    # TODO respect XDG
    return pathlib.Path('./usr/local/share/geant4-data')

def get_tmp_download_dir() -> pathlib.Path:
    # TODO XDG or tempfile.mkdtemp() ?
    return pathlib.Path('/tmp')

def get_config_path() -> pathlib.Path:
    # TODO respect XDG ?
    return pathlib.Path('./usr/etc/g4dsdw/config.json')
