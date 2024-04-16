import argparse
import logging

from . import __version__
from . import installer, lister

# Install datasets:
#  g4dsdw install g4 VERSION
#  g4dsdw install DATASET VERSION
# Geant4 versions / datasets will be marked as installed in a config file

# Uninstall datasets:
#  g4dsdw uninstall g4 VERSION
#  g4dsdw uninstall DATASET VERSION
# Marks Geant4 versions / datasets as uninstalled, only removes datasets
# from disk when there is no other installed Geant4 version dependent on them.

# Upgrade datasets:
#  g4dsdw upgrade g4 VERSION [--old-version OLDVERSION]
# Upgrades datasets to a new Geant4 version

# List datasets:
#  g4dsdw list g4 [--installed]
#  g4dsdw list datasets [--installed]

# Export environment:
#  g4dsdw env [ARGS...]
# If arguments given, evaluate arguments as system call with Geant4 environment
# If no arguments given, print shell script to export Geant4 variables

# Manage environment:
#  g4dsdw setenv use g4 VERSION
#  g4dsdw setenv use DATASET VERSION
#  g4dsdw setenv list
#  g4dsdw setenv reset

# Repair datasets:
#  g4dsdw repair [--all]
#  g4dsdw repair g4 VERSION [--force]
#  g4dsdw repair DATASET VERSION
# Downloads and installs datasets again (e.g. if internet connection was lost)

# Usage within package managers:
#  g4dsdw pm install VERSION
#  g4dsdw pm upgrade VERSION
#  g4dsdw pm uninstall VERSION
#  g4dsdw pm purge
# Marks G4 version as installed by package manager allowing for easy upgrades

def run_argparse(args: list[str]) -> argparse.Namespace:

    parser = argparse.ArgumentParser(description='Geant4 dataset downloader')

    parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
    parser.add_argument('--version', action='version', version=f'g4dsdw {__version__}')

    subparsers = parser.add_subparsers(title='Subcommands', required=True)

    install_help = 'Install single datasets or collection for a specific Geant4 version'
    parser_install = subparsers.add_parser('install', help=install_help, description=install_help)
    parser_install.add_argument('what', help='what to install (either g4 or name of a dataset)')
    parser_install.add_argument('version', help='version to be installed')
    parser_install.set_defaults(subcmd='install')

    uninstall_help = 'Unstall single datasets or collection for a specific Geant4 version'
    parser_uninstall = subparsers.add_parser('uninstall', help=uninstall_help, description=uninstall_help)
    parser_uninstall.add_argument('what', help='what to uninstall (either g4 or name of a dataset)')
    parser_uninstall.add_argument('version', help='version to be marked for removal')
    parser_uninstall.set_defaults(subcmd='uninstall')

    list_help = 'List available and installed datasets and dataset collections'
    parser_list = subparsers.add_parser('list', help=list_help, description=list_help)
    parser_list.add_argument('what', help='what to list (g4 for Geant4 versions, ds for all datasets or dataset name)')
    parser_list.add_argument('-d', '--detailed', action='store_true', help='produce more detailed output')
    parser_list.add_argument('-i', '--installed', action='store_true', help='only list installed items')
    parser_list.set_defaults(subcmd='list')

    return parser.parse_args(args=args)


def main(args: list[str]) -> int:
    # register CLI options and parse args
    options = run_argparse(args)
    # register logger
    log_level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(message)s')

    # TODO use try catch + then error code

    subcmd = options.subcmd
    if subcmd == 'install':
        what = options.what
        if what == 'g4':
            installer.install_g4(options.version)
        else:
            installer.install_dataset(what, options.version, True)
    elif subcmd == 'uninstall':
        what = options.what
        if what == 'g4':
            installer.uninstall_g4(options.version)
        else:
            installer.uninstall_dataset(what, options.version)
    elif subcmd == 'list':
        what = options.what
        if options.installed:
            if what == 'g4':
                lister.list_installed_g4vers()
            elif what == 'ds':
                lister.list_installed_datasets()
            else:
                lister.list_installed_dataset_versions(what)
        else:
            if what == 'g4':
                lister.list_all_g4vers(options.detailed)
            elif what == 'ds':
                lister.list_all_datasets(options.detailed)
            else:
                lister.list_all_dataset_versions(what)

    return 0
