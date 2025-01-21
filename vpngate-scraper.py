#!/usr/bin/python3

"""
vpngate-scraper.py

A scraper for vpngate.net
"""

import os
import sys
import base64
import requests

# Configuration
debug = False
outdir = "~/Downloads/vpngate_scraper/"

def parse_row_data(outdir, row):
	""" Determine if the server detailed in this row is worthwhile, and
	if so, extract and save relevant details
	
	Arguments:
		outdir - dirpath - Location to write server configs to
		row - dict - VPN server data
		
	Returns:
		None
	"""
	
	row_data = (hostname, ip, score, ping, speed, country_long, country_short, num_vpn_sessions, uptime, total_users, total_traffic, log_type, operator, message, openvpn_config_data_base64) = row.split(",")
	ovpn_file = os.path.join(outdir, "{0}-{1}.ovpn".format(row_data[5], row_data[1]))
	with open(ovpn_file, "w") as f:
		f.write(base64.b64decode(row_data[14]).decode("utf-8"))
		
	return None

# Begin execution
if __name__ == "__main__":
	outdir = os.path.expanduser(outdir)
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	os.system("rm {}".format(os.path.join(outdir, "*")))
	
	try:
		response = requests.get("https://www.vpngate.net/api/iphone/")
		f = open(os.path.join(outdir, "rawdata.csv"), "w")
		f.write(response.text)
		f.close()
		
		if debug == True:
			print("[DEBUG] Response from server obtained!")
			
	except requests.exceptions.RequestException as err_msg:
		print(err_msg)
		exit(0)
		
	with open(os.path.join(outdir, "rawdata.csv"), "r") as csv_file:
		rows = csv_file.readlines()
		
		c = 0
		last = len(rows)
		for row in rows:
			c += 1
			if c < 3 or c == last:
				continue
				
			parse_row_data(outdir, row)
			
	exit(0)
