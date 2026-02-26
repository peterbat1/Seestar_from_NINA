#!/usr/bin/env python3
#
#  Seestar_connection_test_alpyca.py
#  
#  This script is an adaptation of test or example code found in
#  the documentation for the Python Alpyca module which provides
#  an interface to ASCOM Alpaca devices.
#
#  
#  Peter D. Wilson 2026-02-16
#  

import sys
import time
from alpaca.telescope import *
from alpaca.exceptions import *

############
# Edit the values assigned to this constant to show the IP address
# and port number you have discovered for your Seestar on your local
# network
############

SEESTAR_IP = '192.168.1.22:32323'

def main(args):
	T = Telescope(SEESTAR_IP, 0)
	try:
		T.Connect() # Asynchronous in Platform 7
		while T.Connecting:
			time.sleep(0.5)
		print(f'Connected to {T.Name}')
		print(T.Description)
		T.Tracking = True # Needed for slewing (see below)
		print('Starting slew...')
		T.SlewToCoordinatesAsync(T.SiderealTime + 2, 50) # 2 hrs east of meridian
		while(T.Slewing):
			time.sleep(5) # What do a few seconds matter?
		print('... slew completed successfully.')
		print(f'RA={T.RightAscension} DE={T.Declination}')
		print('Turning off tracking then attempting to slew...')
		T.Tracking = False
		T.SlewToCoordinatesAsync(T.SiderealTime + 2, 55) # 5 deg slew N
		# This will fail for tracking being off
		print("... you won't get here!")
	except Exception as e: # Should catch specific InvalidOperationException
		print(f'Caught {type(e).__name__}')
		print(f' Slew failed: {e.message}') # Using exception named properties
	finally:	# Assure that you disconnect
		print("Disconnecting...")
		T.Connected = False
	
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
