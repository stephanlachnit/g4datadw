datasets = {
    'G4NDL': {
        'env_var': 'G4NEUTRONHPDATA',
        'versions': {
            '4.7': 'https://cern.ch/geant4-data/datasets/G4NDL.4.7.tar.gz',
            '4.6': 'https://cern.ch/geant4-data/datasets/G4NDL.4.6.tar.gz',
            '4.5': 'https://cern.ch/geant4-data/datasets/G4NDL.4.5.tar.gz',
        }
    },
    'G4EMLOW': {
        'env_var': 'G4LEDATA',
        'versions': {
            '8.2': 'https://cern.ch/geant4-data/datasets/G4EMLOW.8.2.tar.gz',
            '8.1': 'https://cern.ch/geant4-data/datasets/G4EMLOW.8.1.tar.gz',
            '8.0': 'https://cern.ch/geant4-data/datasets/G4EMLOW.8.0.tar.gz',
            '7.13': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.13.tar.gz',
            '7.12': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.12.tar.gz',
            '7.11': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.11.tar.gz',
            '7.10': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.10.tar.gz',
            '7.9.1': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.9.1.tar.gz',
            '7.9': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.9.tar.gz',
            '7.8': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.8.tar.gz',
            '7.7': 'https://cern.ch/geant4-data/datasets/G4EMLOW.7.7.tar.gz',
        }
    },
    'PhotonEvaporation': {
        'env_var': 'G4LEVELGAMMADATA',
        'versions': {
            '5.7': 'https://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.7.tar.gz',
            '5.6': 'https://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.6.tar.gz',
            '5.5': 'https://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.5.tar.gz',
            '5.4': 'https://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.4.tar.gz',
            '5.3': 'https://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.3.tar.gz',
        }
    },
    'RadioactiveDecay': {
        'env_var': 'G4RADIOACTIVEDATA',
        'versions': {
            '5.6': 'https://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.6.tar.gz',
            '5.5': 'https://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.5.tar.gz',
            '5.4': 'https://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.4.tar.gz',
            '5.3': 'https://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.3.tar.gz',
        }
    },
    'G4PARTICLEXS': {
        'env_var': 'G4PARTICLEXSDATA',
        'versions': {
            '4.0': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.4.0.tar.gz',
            '3.1.1': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.3.1.1.tar.gz',
            '3.1': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.3.1.tar.gz',
            '3.0': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.3.0.tar.gz',
            '2.1': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.2.1.tar.gz',
            '1.1': 'https://cern.ch/geant4-data/datasets/G4PARTICLEXS.1.1.tar.gz',
        }
    },
    'G4PII': {
        'env_var': 'G4PIIDATA',
        'versions': {
            '1.3': 'https://cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz',
        }
    },
    'RealSurface': {
        'env_var': 'G4REALSURFACEDATA',
        'versions': {
            '2.2': 'https://cern.ch/geant4-data/datasets/G4RealSurface.2.2.tar.gz',
            '2.1.1': 'https://cern.ch/geant4-data/datasets/G4RealSurface.2.1.1.tar.gz',
        }
    },
    'G4SAIDDATA': {
        'env_var': 'G4SAIDXSDATA',
        'versions': {
            '2.0': 'https://cern.ch/geant4-data/datasets/G4SAIDDATA.2.0.tar.gz',
        }
    },
    'G4ABLA': {
        'env_var': 'G4ABLADATA',
        'versions': {
            '3.1': 'https://cern.ch/geant4-data/datasets/G4ABLA.3.1.tar.gz',
        }
    },
    'G4INCL': {
        'env_var': 'G4INCLDATA',
        'versions': {
            '1.0': 'https://cern.ch/geant4-data/datasets/G4INCL.1.0.tar.gz',
        }
    },
    'G4ENSDFSTATE': {
        'env_var': 'G4ENSDFSTATEDATA',
        'versions': {
            '2.3': 'https://cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.3.tar.gz',
            '2.2': 'https://cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.2.tar.gz',
        }
    },
    'G4TENDL': {
        'env_var': 'G4PARTICLEHPDATA',
        'versions': {
            '1.4': 'https://cern.ch/geant4-data/datasets/G4TENDL.1.4.tar.gz',
            '1.3.2': 'https://cern.ch/geant4-data/datasets/G4TENDL.1.3.2.tar.gz',
        }
    },
}

geant4_versions = {
    # 11.1 series
    '11.1': '11.1.0',
    '11.1.2': '11.1.0',
    '11.1.1': '11.1.0',
    '11.1.0': {
        'G4NDL': '4.7',
        'G4EMLOW': '8.2',
        'PhotonEvaporation': '5.7',
        'RadioactiveDecay': '5.6',
        'G4PARTICLEXS': '4.0',
        'G4PII': '1.3',
        'RealSurface': '2.2',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.3',
        'G4TENDL': '1.4',
    },
    # 11.0 series
    '11.0': '11.0.0',
    '11.0.4': '11.0.0',
    '11.0.3': '11.0.0',
    '11.0.2': '11.0.0',
    '11.0.1': '11.0.0',
    '11.0.0': {
        'G4NDL': '4.6',
        'G4EMLOW': '8.0',
        'PhotonEvaporation': '5.7',
        'RadioactiveDecay': '5.6',
        'G4PARTICLEXS': '4.0',
        'G4PII': '1.3',
        'RealSurface': '2.2',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.3',
        'G4TENDL': '1.4',
    },
    # 10.7 series
    '10.7': '10.7.2',
    '10.7.4': '10.7.2',
    '10.7.3': '10.7.2',
    '10.7.2': {
        'G4NDL': '4.6',
        'G4EMLOW': '7.13',
        'PhotonEvaporation': '5.7',
        'RadioactiveDecay': '5.6',
        'G4PARTICLEXS': '3.1.1',
        'G4PII': '1.3',
        'RealSurface': '2.2',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.3',
        'G4TENDL': '1.3.2',
    },
    '10.7.1': '10.7.0',
    '10.7.0': {
        'G4NDL': '4.6',
        'G4EMLOW': '7.13',
        'PhotonEvaporation': '5.7',
        'RadioactiveDecay': '5.6',
        'G4PARTICLEXS': '3.1.1',
        'G4PII': '1.3',
        'RealSurface': '2.2',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.3',
        'G4TENDL': '1.4',
    },
    # 10.6 series
    '10.6': '10.6.1',
    '10.6.3': '10.6.1',
    '10.6.2': '10.6.1',
    '10.6.1': {
        'G4NDL': '4.6',
        'G4EMLOW': '7.9.1',
        'PhotonEvaporation': '5.5',
        'RadioactiveDecay': '5.4',
        'G4PARTICLEXS': '2.1',
        'G4PII': '1.3',
        'RealSurface': '2.1.1',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.2',
    },
    '10.6.0': {
        'G4NDL': '4.6',
        'G4EMLOW': '7.9',
        'PhotonEvaporation': '5.5',
        'RadioactiveDecay': '5.4',
        'G4PARTICLEXS': '2.1',
        'G4PII': '1.3',
        'RealSurface': '2.1.1',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.2',
    },
    # 10.5 series
    '10.5': '10.5.0',
    '10.5.1': '10.5.0',
    '10.5.0': {
        'G4NDL': '4.5',
        'G4EMLOW': '7.7',
        'PhotonEvaporation': '5.3',
        'RadioactiveDecay': '5.3',
        'G4PARTICLEXS': '2.1',
        'G4PII': '1.3',
        'RealSurface': '2.1.1',
        'G4SAIDDATA': '2.0',
        'G4ABLA': '3.1',
        'G4INCL': '1.0',
        'G4ENSDFSTATE': '2.2',
    },
}


def resolve_g4_link(version: str) -> str:
    """Resolve link to a Geant4 version in database

    Args:
        version: Geant4 version to resolve
    """
    g4ver_entry = geant4_versions.get(version)
    if g4ver_entry is None:
        raise Exception(f'Geant4 version {version} is not in database, please run `g4dsdw list g4` for supported versions')
    if type(g4ver_entry) is str:
        # version is a link, return value
        return g4ver_entry
    else:
        # version is not a link, return itself
        return version
