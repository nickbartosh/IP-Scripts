from collections import defaultdict

ip_list =  ['192.168.15.15','10.10.10.10','22.23.24.25','104.15.200.206','104.16.202.200','104.15.200.201']

def split_ip(ip):
    return tuple(int(part) for part in ip.split('.'))

def print_list(my_list):
    for x in my_list:
        print(f'{x}')

def sort_key(ip_addr):
    return split_ip(ip_addr)

def main():
    ipCount = defaultdict(int)
    d = defaultdict(int)
    
    print("IP Sorting\n\n")
    print_list(ip_list)
    
    sorted_list = sorted(ip_list, key=sort_key)
    print_list(sorted_list)


if __name__ == "__main__":
    print("items")
    main()
  