import argparse
import csv
import os

def import_file():
    filename = args.filename
    print(f'Importing {filename}')
    if not os.path.exists(filename)
        parser.print_help()
        print(f'\n The file {filename} cannot be found or you do not have '
              'permission to ope the file.')

def main():


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
        help="Display error information",
        action="store_true")
    
    parser.add_argument("-f", "--filename",
        help="The file of IP addresses and ranges to be imported")
    
    parser.add_argument("-p", "--print_ips",
        help="Print the list of IPs found in the file (this does not create the config)")
    
    args = parser.parse_args()
    main()