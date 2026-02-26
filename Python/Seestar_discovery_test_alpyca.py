#!/usr/bin/env python3
#
#  Seestar_discovery_test_alpyca.py
#  
#  This script is an adaptation of test or example code found in
#  the documentation for the Python Alpyca module which provides
#  an interface to ASCOM Alpaca devices.
#  
#  See: https://ascom-standards.org/alpyca/alpaca.discovery.html
#  
#  Peter D. Wilson 2026-02-16
# 
#  NOTE: There can be delay of upto a few minutes for the discovery
#  process to complete...be patient!

import sys
from alpaca import discovery

def main(args):
	svrs = discovery.search_ipv4() # Note there is an IPv6 function as well
	print(svrs)
	
	return 0

if __name__ == '__main__':
