import sys
import argparse
from modules import *

VERSION="v1.0.0"

def main():

    if '--help' in sys.argv or '-h' in sys.argv:
        print(f"version: {VERSION}")

    parser = argparse.ArgumentParser(description="Search the database for specimen information.")
    parser.add_argument('--version','-v', action='version', version=f'%(prog)s {VERSION}')
    subparsers = parser.add_subparsers(dest="command", required=True)

    # sample id
    parser_sid = subparsers.add_parser("sample_ID", aliases=['sid'], help="Search by sample ID", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_sid.add_argument("--sample_id", "-s", required=True, help="sample id")
    parser_sid.add_argument("--verbose","-v", required=False, help="Show details", action='store_true')
    parser_sid.add_argument("--directory","-d", required=False, help="parent analytical directory", default="/data1/data/result")
    parser_sid.set_defaults(func=run_sampleid)

    # Patient id
    parser_pid = subparsers.add_parser("patient_ID", aliases=['pid'], help="Search by Patient ID", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_pid.add_argument("--patient_id", "-p", required=True, help="Patient ID")
    parser_pid.add_argument("--verbose","-v", required=False, help="Show details", action='store_true')
    parser_pid.add_argument("--directory","-d", required=False, help="parent analytical directory", default="/data1/data/result")
    parser_pid.set_defaults(func=run_patientid)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":

    main()


