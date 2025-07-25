import sys
import argparse
from modules import *

VERSION="v1.1.0"

def main():

    if '--help' in sys.argv or '-h' in sys.argv:
        print(f"version: {VERSION}")

    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--sample_id", "-s", required=False, help="sample id")
    parser.add_argument("--patient_id", "-p", required=False, help="Patient ID")
    parser.add_argument("--verbose", required=False, help="Show details", action='store_true')
    parser.add_argument("--directory","-d", required=False, help="parent analytical directory", default="/data1/data/result")
    parser.add_argument("--version","-v", action='version', version=f'%(prog)s {VERSION}')

    args = parser.parse_args()
    run_info(args)

if __name__ == "__main__":

    main()

