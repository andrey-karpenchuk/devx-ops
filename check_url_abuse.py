#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://urlhaus.abuse.ch/browse/   search in abuse.ch
'''
import requests, json, sys

URL_ABUSECH = 'https://urlhaus-api.abuse.ch/v1/host/'

def get_abuse(host):
    data_json = {
        'host' : host
    }
    response = requests.request("POST", URL_ABUSECH, data=data_json, timeout=15)
    # response_json = response.json()
    data = response.json()
    if data['query_status'] == 'no_results':
        result = 'In urlhouse this {} was not found'.format(host)
    else:
        result = '{} found in {} blacklists URLhouse'.format(host, data['url_count'])
    print(result)
    return(result)

if __name__ == '__main__':
    list_arg = sys.argv[1:]
    for host in list_arg:
        get_abuse(host)
