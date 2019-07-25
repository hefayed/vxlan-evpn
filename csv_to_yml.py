#!/usr/bin/env python
import csv
import yaml

l2vni_data = []
with open('/home/contiv/vxlan-evpn/l2vni_vars.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        l2vni_data.append(row['vlan_id'])


l2vni_vars = list(map(int, l2vni_data))

with open('/home/contiv/vxlan-evpn/roles/l2vni_overlay/vars/main.yml', 'a') as outfile:
    
    outfile.write(yaml.dump({'vlan_id': l2vni_vars}, default_flow_style=False))
