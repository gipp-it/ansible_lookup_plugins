#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from hcloud import Client
from ansible.utils.display import Display

API_TOKEN = "API_TOKEN"

client = Client(token=API_TOKEN)

class LookupModule(LookupBase):
    def run(self, terms=None, variables=None, **kwargs):
        servers = client.servers.get_all()
        ips = []
        for server in servers:
            ips.append({'ip': server.public_net.ipv4.ip, 'name': server.name})
        return ips

if __name__ == "__main__":
    l = LookupModule()
    print(l.run())