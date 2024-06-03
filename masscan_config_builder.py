import argparse
import csv
import os
import re

from termcolor import colored

#Global constants
REGEX_IPV4 = re.compile("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")

def import_file():
    filename = args.filename
    if filename is None:
        parser.print_help()

        print(colored(f'\n[-] An input file of type text is required.','red'))
        exit()

    print(f'Importing {filename}')
    if os.path.exists(filename):
        with open(filename, "r") as ipFile:
            for line in ipFile:
                match = REGEX_IPV4.match(line)
                print(f'{match}')
    else:
        parser.print_help()
        print(colored(f'\n The file {filename} cannot be found or you do not have '
              'permission to ope the file.','red'))
        exit()


def main():
    import_file()

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