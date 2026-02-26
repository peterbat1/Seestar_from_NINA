#!/usr/bin/env python3
#
#  Seestar_server_info_alpyca.py
#  
#  This script is an adaptation of test or example code found in
#  the documentation for the Python Alpyca module which provides
#  an interface to ASCOM Alpaca devices.
#  
#  See: https://ascom-standards.org/alpyca/alpaca.management.html
#  
#  Peter D. Wilson 2026-02-16; 2026-02-26
#  
#  NOTE: There can be delay of upto a few minutes for the discovery
#        step to complete, so please be patient
#  

import sys
from alpaca import discovery
from alpaca import management

def main(args):
	
	svrs = discovery.search_ipv4()
	print(svrs)
	for svr in svrs:
		print(f"At {svr}")
		print (f"  V{management.apiversions(svr)} server")
		print (f"  {management.description(svr)['ServerName']}")
		devs = management.configureddevices(svr)
		for dev in devs:
			print(f"    {dev['DeviceType']}[{dev['DeviceNumber']}]: {dev['DeviceName']}")
	
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
