#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://hetrixtools.com/    search in hetrixtools database
'''
import requests, json, sys
from IPy import IP

result_dict = {}
URL_HERTIX = 'https://api.hetrixtools.com/v2/'
API_KEY = sys.argv[1]

def check(str_name, host):
    if host == 'ip':
        url = URL_HERTIX + API_KEY + '/blacklist-check/ipv4/' + str_name + '/'
    else:
        url = URL_HERTIX + API_KEY + '/blacklist-check/domain/' + str_name + '/'
    # print(url)
    response = requests.request("GET", url)
    response_json = response.json()

    try:
        if response_json['status'] == 'ERROR':
            result ="Script check IP not work: " + response_json['error_message']
            return(result)
        else:
            # print(response_json)
            result_dict = {
                'blacklisted_count' : response_json['blacklisted_count'],
                'blacklist_check_credits_left' : response_json['blacklist_check_credits_left']
                }
            result = '{} is listed on {} out of {} checked blacklists in hetrix'.format(str_name, result_dict['blacklisted_count'], result_dict['blacklist_check_credits_left'])
            return(result)      
    except:
        return("Script check not work")

def check_ip_or_dns(ip_or_dnsname):
    try:
        IP(ip_or_dnsname)
    except ValueError:
        return check(ip_or_dnsname, 'dnsname')
    return check(ip_or_dnsname, 'ip')

if __name__ == '__main__':
    list_arg = sys.argv[2:]
    for host in list_arg:
        print(check_ip_or_dns(host))
