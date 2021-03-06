#!/usr/bin/env python
import sys
import csv
import yaml
import yamlloader

l2vni_data = []
my_csv_file = '/home/contiv/vxlan-evpn/l2vni_vars.csv'
my_vars_file = '/home/contiv/vxlan-evpn/roles/l2vni_overlay/vars/main.yml'

with open(my_csv_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        l2vni_data.append(row)

with open(my_vars_file) as data:
    data_loaded = yaml.load(data, Loader=yamlloader.ordereddict.CLoader)
    yaml.dump(data_loaded, sys.stdout)

with open(my_vars_file, "w") as file:
    file.write('---\n')
    yaml.dump({'nxos_provider': data_loaded['nxos_provider']}, file, Dumper=yamlloader.ordereddict.CDumper)
    file.write('\n')
    file.write('# vars for creation of l2vni and vlan interface configuration\n')


with open(my_vars_file, "a") as file:
    file.write('\n')
    yaml.dump({'l2vni': l2vni_data}, file, Dumper=yamlloader.ordereddict.CDumper)
