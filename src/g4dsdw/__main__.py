from . import cli

def run_main_and_exit():
    import sys
    sys.exit(cli.main(sys.argv[1:]))

if __name__ == '__main__':
    run_main_and_exit()
