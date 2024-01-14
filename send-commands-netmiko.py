from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_netmiko import netmiko_send_command
from pprint import pprint
from rich import print as rprint
import re
import pandas as pd

from nornir_pyxl.plugins.tasks import pyxl_ez_data

#initialize host file 
#clears content of the host file, making sure of no duplicates

host_zero = open('/home/rodneilr/nornir_automation/inventory/hosts.yaml', 'w')
host_zero.close()


#create host.yaml file

def create_host():
    ipfile = "ip_dump.txt"
    with open(ipfile, 'r') as file:
        device_ips = file.read().splitlines()

    host_up = open('/home/rodneilr/nornir_automation/inventory/hosts.yaml', 'a')
    

    for ips in device_ips:
        host_up.write(f"{ips}:\n")
        host_up.write(f" hostname: \"{ips}\"\n")
        host_up.write(" port: 22\n")
        host_up.write(" username: \n")
        host_up.write(" password: \n")
        host_up.write(" platform: \"ios\"\n")
        #host_up.write("  groups: ")
        host_up.write("\n")
        host_up.write("\n")


create_host()

nr = InitNornir(config_file="config.yaml")
host = nr.inventory.hosts

def nornir_netmiko_textfsm_format(task):
    host_excel = r'/home/rodneilr/nornir_automation/machine.xlsx'

    result=task.run(task=netmiko_send_command, command_string="dir", use_genie=True)
    task.host["facts"] = result.result
    device_items = result.result
    firm_file = re.compile(r"\.bin$", re.IGNORECASE)

    print_result(result)
    print(len(result))


    #for x in range(0,47):
        #if "trunk" in task.host['facts'][x]['admin_mode']:
            #print(task.host, end='')
            #print(" has a trunk port on interface " + task.host['facts'][x]['interface'])

    #host_to_excel = task.run(task=WriteExcel, file=host_excel, data=device_items)
    
    
    #print_result(host_to_excel)
    #rint (len(device_items))
    
    
    #df = pd.DataFrame.from_dict(device_items)

    #df.to_excel(host_excel)
    #with pd.ExcelWriter(host_excel,mode='a', if_sheet_exists="replace") as writer:  
     #df.to_excel(writer)
    
    
    #rprint(device_items)
    #rprint(type(interfaces))

    #grab machine information
    #for items in device_items:
        #rprint(interface)
        #rprint(type(interface))
        #rprint(items["hostname"]+ "," + items["running_image"])

    #print(len(device_items))
    #rprint(device_items)
    

    #while index < len(device_items):
        #for key in device_items[index]:
        #if device_items[index]['name'] in firm_file.pattern(device_items):
    
    
    #bin_files = [file['name'] for file in device_items if firm_file.search(file['name'])]
    #rprint(host, bin_files)
    



results=nr.run(task=nornir_netmiko_textfsm_format)
import ipdb;
ipdb.set_trace()
   


