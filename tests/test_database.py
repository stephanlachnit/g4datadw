
from g4dsdw.database import datasets, geant4_versions

for this_g4ver, this_g4ver_datasets in geant4_versions.items():
    print(f'Geant4 {this_g4ver}')
    if type(this_g4ver_datasets) is str:
        continue
    for this_dataset, this_datasetver in this_g4ver_datasets.items():
        if not this_dataset in datasets:
            print('throw')
        dataset_vers = datasets[this_dataset]['versions']
        if not this_datasetver in dataset_vers:
            print('throw')
        print(f'{dataset_vers[this_datasetver]}')
