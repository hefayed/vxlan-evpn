#!/usr/bin/env python
import csv
import yaml

l2vni_data = []
with open('data.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        l2vni_data.append(row['vlan_id'])


l2vni_vars = list(map(int, l2vni_data))

with open('l2vni_vars.yml', 'w+') as outfile:
    outfile.write('---\n')
    outfile.write(yaml.dump({'L2VNI': l2vni_vars}, default_flow_style=False))
