import requests
import json
import yaml
import requests
import sys
import argparse

class HttpCall(object):
    def __init__(self, IP):
        self.ip = IP
        self.reval = None

    # HTTP methods then print return value 
    def create_server_type(self):
        pass 
    def create_server_asset(self):
        pass
    def delete_server_type(selt):
        pass
    def update_server_type(self):
        pass
    def get_server_type(self):
        post_route = 'asset_type?type=server'
        route = self.ip + post_route
        self.reval = requests.get(route)
        self.print_json() 
    def update_server_assest(self):
        pass
    def delete_server_assest(self):
        pass
    def get_server(self):
        post_route = 'asset?type=server'
        route = self.ip + post_route
        self.reval = requests.get(route)
        self.print_json()
    def get_server_distinct(self):
        post_route = 'asset/distinct?type=server&distinct_key=datacenter'
        route = self.ip + post_route
        self.reval = requests.get(route)
        self.print_json()
    def print_json(self):
        if self.reval:
            print json.dumps(self.reval.json(), sort_keys=True, indent=4,
                         separators=(',', ':'))

def main(**kwargs):
    hostIP = None
    http_method = None

    for key, value in kwargs.iteritems():
        if key == 'hostIP':
            hostIP = value
        if key == 'http_method':
            http_method = value
    # Choose method types
    httpcall = HttpCall(hostIP)
    if http_method == 'get_server':
        httpcall.get_server()
    elif http_method == 'get_server_type':
        httpcall.get_server_type()
    elif http_method == 'get_server_distinct':
        httpcall.get_server_distinct()

if __name__ == "__main__":
    # args parser
    tool_description = """
                       Simple:
                           python http_tool.py -m get_server
                       """ 
    parser = argparse.ArgumentParser(description=tool_description)
    parser.add_argument('--method', '-m', nargs='?', help=
                        """
                        HTTP method, now
                        only support GET methods <get_server/ get_server_type
                        / get_server_distinct>.
                        """)
    parser.add_argument('--ip', '-i', nargs='?', 
                        default='http://10.14.210.61:5000/api/v1/', 
                        help=
                        """ 
                        IP address, default is
                        iNova node, no need to fill in.""")
    args = parser.parse_args()

    main(http_method=args.method, hostIP=args.ip)
