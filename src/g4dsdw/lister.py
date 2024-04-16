from collections import defaultdict

from . import config, database

def list_all_g4vers(detailed: bool) -> None:
    if detailed:
        reverse_dict = defaultdict(list)
        for g4ver, entry in database.geant4_versions.items():
            # if entry is link, don't print but store for comment
            if type(entry) is str:
                reverse_dict[entry].append(g4ver)
                continue
            # entry is proper, so let's go get printing
            main_g4ver_name = g4ver
            alt_names_str = ''
            if len(reverse_dict[g4ver]) > 0:
                alt_names_str = ' (also'
                main_g4ver_name = reverse_dict[g4ver][0]
                for count in range(1, len(reverse_dict[g4ver])):
                    alt_names_str += ' ' + reverse_dict[g4ver][count] + ','
                alt_names_str += ' ' + g4ver + ')'
            print(f'Geant4 {main_g4ver_name}{alt_names_str}')
            # print contained datasets if detailed option
            for dataset, dataset_version in entry.items():
                print(f'  {dataset}: {dataset_version}')
    else:
        print('Geant4 versions in the database:')
        for g4ver in database.geant4_versions.keys():
            print(f'  {g4ver}')
        print('Run `g4dsdw list g4 -d` for information on the contained datasets')

def list_installed_g4vers() -> None:
    pass

def list_all_datasets(detailed: bool) -> None:
    if detailed:
        pass
    else:
        print('Datasets in the database:')
        for dataset, dataset_entry in database.datasets.items():
            dataset_versions = dataset_entry['versions'].keys()
            versions_str = '(version'
            if len(dataset_versions) > 1:
                versions_str += 's'
                for dataset_version in dataset_versions:
                    versions_str += ' ' + dataset_version + ','
                versions_str = versions_str[:-1] + ')'
            else:
                versions_str += ' ' + dataset_version + ')'
            print(f'  {dataset} {versions_str}')
        print('Run `g4dsdw list ds -d` for information on the dependent Geant4 versions')

def list_installed_datasets() -> None:
    pass

def list_all_dataset_versions(version: str) -> None:
    pass

def list_installed_dataset_versions(version: str) -> None:
    pass
