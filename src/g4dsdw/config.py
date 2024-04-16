import json
import os

from .private.singleton import Singleton
from . import paths

class Config(metaclass=Singleton):
    _config_path = paths.get_config_path()
    _config = dict()

    def __init__(self) -> None:
        # ensure folder for config exists
        os.makedirs(self._config_path.parent, exist_ok=True)
        # read existing config
        self.load()

    def get_installed_g4_versions(self) -> list[str]:
        """Gets list of installed Geant4 versions

        Note:
            \"Geant4 version\" refers to selection of corresponding datasets

        Returns:
            List of the installed Geant4 versions
        """
        installed_g4_versions = self._config.get('installed_g4_versions')
        if installed_g4_versions is None:
            return list[str]()
        else:
            return installed_g4_versions

    def is_g4_installed(self, version: str) -> bool:
        """Check if a specific Geant4 version is installed

        Note:
            \"Geant4 version\" refers to selection of corresponding datasets

        Args:
            version: Version of the Geant4 version to check

        Returns:
            If the Geant4 version is installed
        """
        return version in self.get_installed_datasets()

    def set_g4_installed(self, version: str) -> None:
        """Set Geant4 version as installed

        Note:
            \"Geant4 version\" refers to selection of corresponding datasets

        Datastructure:
            See :automethod:`get_installed_g4_versions()`

        Args:
            version: Version to mark as installed
        """
        installed_g4_versions = self._config.get('installed_g4_versions')
        if installed_g4_versions is None:
            self._config['installed_g4_versions'] = [version]
        elif version not in installed_g4_versions:
            installed_g4_versions.append(version)
            installed_g4_versions.sort()
            self._config['installed_g4_versions'] = installed_g4_versions
        # write new config
        self.write()

    def set_g4_uninstalled(self, version: str) -> None:
        """Set Geant4 version as uninstalled

        Note:
            \"Geant4 version\" refers to selection of corresponding datasets

        Datastructure:
            See :automethod:`get_installed_g4_versions()`

        Args:
            version: Version to mark as uninstalled
        """
        installed_g4_versions = self._config.get('installed_g4_versions')
        if installed_g4_versions is None:
            raise Exception(f'No Geant4 versions installed, cannot uninstall Geant4 version {version}')
        elif version not in installed_g4_versions:
            raise Exception(f'Geant4 version {version} installed, cannot uninstall it')
        else:
            self._config['installed_g4_versions'].remove(version)
        # write new config
        self.write()

    def get_installed_datasets_dict(self) -> dict:
        """Get dictionary of installed datasets

        Datastructure:
            \"installed_datasets\": {
                \"<dataset>\": {
                    \"<version>\": {
                        \"manual\": <bool>
                    }
                }
            }

        Retruns:
            Dictionary with the installed datasets according the above datastructure
        """
        installed_datasets = self._config.get('installed_datasets')
        if installed_datasets is None:
            return dict()
        return installed_datasets

    def get_installed_datasets_list(self) -> list[tuple[str, list[str]]]:
        """Get list of installed datasets with the installed versions

        Returns:
            List of installed datasets with the installed versions
        """
        # Note: for datastructure see get_installed_datasets_dict
        out = list[tuple[str, list[str]]]()
        for dataset, dataset_dict in self.get_installed_datasets_dict().items():
            versions = list[str](dataset_dict.keys())
            item = tuple[str, list[str]]((dataset, versions))
            out.append(item)
        return out

    def is_dataset_installed(self, dataset: str, version: str = None) -> bool:
        """Check if a specific dataset is installed

        Args:
            dataset: Name of the dataset to check
            version: Version of the dataset to check or :obj:`None` for any version

        Returns:
            If the dataset in the specified version is installed
        """
        # Note: for datastructure see get_installed_datasets_dict
        dataset_dict_entry = self.get_installed_datasets_dict().get(dataset)
        if dataset_dict_entry is None:
            # dataset not installed
            return False
        if version is None:
            # dataset installed, return true since no check for version requested
            return True
        version_dict_entry = dataset_dict_entry.get(version)
        if version_dict_entry is None:
            # dataset installed but not in correct version
            return False
        # dataset installed in correct version
        return True

    def is_dataset_manual(self, dataset, version) -> bool | None:
        """Check if a specific dataset is manually installed

        Returns:
            If the dataset is manually installed or :obj:`None` if not installed at all
        """
        # Note: for datastructure see get_installed_datasets_dict
        if self.is_dataset_installed(dataset, version):
            return self.get_installed_datasets_dict()[dataset][version]
        return None

    def set_dataset_installed(self, dataset: str, version: str, manual: bool):
        """Set version of a dataset as (manually) installed

        Args:
            dataset: Name of the dataset to be marked as installed
            version: Version of the dataset to be marked as installed
            manual: If the dataset should be marked as manually installed
        """
        # Note: for datastructure see get_installed_datasets_dict
        installed_datasets = self._config.get('installed_datasets')
        if installed_datasets is None:
            # no datasets installed, add entry
            self._config['installed_datasets'] = {
                dataset: {
                    version: {
                        "manual": manual
                    }
                }
            }
        else:
            dataset_dict_entry = installed_datasets.get(dataset)
            if dataset_dict_entry is None:
                # dataset not installed, add entry
                self._config['installed_datasets'][dataset] = {
                    version: {
                        "manual": manual
                    }
                }
            else:
                # dataset installed, add/overwrite version entry
                self._config['installed_datasets'][dataset][version] = {
                    "manual": manual
                }
        # write new config
        self.write()

    def set_dataset_uninstalled(self, dataset: str, version: str) -> None:
        """Set version of dataset as uninstalled

        Args:
            dataset: Name of the dataset to be marked as uninstalled
            version: Version of the dataset to be marked as uninstalled
        """
        # Note: for datastructure see get_installed_datasets_dict
        installed_datasets = self._config.get('installed_datasets')
        if installed_datasets is None:
            # no datasets installed
            raise Exception(f'No datasets installed, cannot uninstall {dataset} version {version}')
        dataset_dict_entry = installed_datasets.get(dataset)
        if dataset_dict_entry is None:
            # dataset not installed
            raise Exception(f'{dataset} not installed, cannot uninstall version {version}')
        # dataset installed, check version
        if dataset_dict_entry.get(version) is None:
            # version not installed
            raise Exception(f'{dataset} version {version} not installed, cannot uninstall it')
        dataset_dict_entry.pop(version)
        # check if any version is installed
        if not dataset_dict_entry:
            # no version installed, remove dataset from list
            self._config['installed_datasets'].pop(dataset)
        else:
            self._config['installed_datasets'][dataset] = dataset_dict_entry
        # write new config
        self.write()

    def load(self) -> None:
        """Try loading config from file
        """
        try:
            with open(self._config_path, 'r') as config_file:
                self._config = json.load(config_file)
        except FileNotFoundError:
            return

    def write(self) -> None:
        """Write current config to file
        """
        with open(self._config_path, 'w') as config_file:
            json.dump(self._config, config_file, indent=4, sort_keys=True)
