#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://urlhaus.abuse.ch/browse/   search in abuse.ch
'''
import requests, json, sys
import argparse

URL_ABUSECH = 'https://urlhaus-api.abuse.ch/v1/host/'

def arg_parse():
    parser = argparse.ArgumentParser(description='Get argument parser')
    parser.add_argument('--first', type=str, help='Head branch for compare')
    parser.add_argument('--second', type=str, help='Against branch for compare')
    parser.add_argument('--tree', type=str, help='Against branch for compare')
    args = parser.parse_args()

    result = {}
    result['first'] = args.first
    result['second'] = args.second
    result['tree'] = args.tree

    return result

def get_abuse(host):
    data_json = {
        'host' : host
    }
    response = requests.request("POST", URL_ABUSECH, data=data_json, timeout=15)
    response_json = response.json()
    data = response.json()
    print(data)
    if data['query_status'] == 'no_results':
        result = 'In urlhouse this {} was not found'.format(host)
    else:

        result = '{} found in {} blacklists URLhouse!'.format(host, data['url_count'])
    print(result)
    return(result)

if __name__ == '__main__':
    print('olololo')
    list_arg = arg_parse()
    print(list_arg)
    for host in list_arg:
        get_abuse(list_arg[host])
