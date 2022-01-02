#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from datetime import datetime
import rancher
from requests.auth import HTTPBasicAuth
import requests
import json
import urllib3
from ansible.utils.display import Display

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

display = Display()
URL = "URL"
ACCESS_KEY = "ACCESS_KEY"
SECRET_KEY = "SECRET_KEY"
CLUSTER_ID = "CLUSTER_ID"

class LookupModule(LookupBase):
    def run(self, terms=None, variables=None, **kwargs):
        req = requests.get(URL, auth=(ACCESS_KEY, SECRET_KEY))
        data = req.json()
        ip = []
        for node in data['data']:
            display.debug("Nodes: %s" % ip)
            if node['unschedulable'] is False and node['worker'] is True and node['clusterId'] == CLUSTER_ID:
                ip.append(node['externalIpAddress'])
        return ip

if __name__ == "__main__":
    look_up = LookupModule()
    print(look_up.run())
