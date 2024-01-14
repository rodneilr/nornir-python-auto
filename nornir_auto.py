from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_ping, napalm_configure
from nornir_netmiko import netmiko_send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

result = nr.run(task=napalm_ping, dest='10.10.20.1')
device_items = result.result
#print_result(result)
rprint(device_items)