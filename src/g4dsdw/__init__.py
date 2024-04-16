"""
g4dsdw (Geant4 dataset downloader)
"""

# get version via importlib
from importlib.metadata import version
__version__ = version('g4dsdw')
del version

# import all public components
from g4dsdw import cli, config, database, installer, paths
