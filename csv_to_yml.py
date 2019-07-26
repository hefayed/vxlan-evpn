#!/usr/bin/env python
import sys
import csv
import ruamel.yaml

l2vni_data = []
my_csv_file = '/home/contiv/vxlan-evpn/l2vni_vars.csv'
my_vars_file = '/home/contiv/vxlan-evpn/roles/l2vni_overlay/vars/main.yml'

with open(my_csv_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        l2vni_data.append(row['vlan_id'])


l2vni_vars = list(map(int, l2vni_data))


with open(my_vars_file) as data:
    data_loaded = ruamel.yaml.round_trip_load(data)
    del data_loaded['vlan_id'][:]
    data_loaded['vlan_idI'] = l2vni_vars
    ruamel.yaml.round_trip_dump(data_loaded, sys.stdout, block_seq_indent=1)

with open(my_vars_file, "w") as file:
    file.write('---\n')
    ruamel.yaml.round_trip_dump(data_loaded, file)
