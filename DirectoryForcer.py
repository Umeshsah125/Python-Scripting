"""
This script will enumerate the directory of given domains
Conditions: write only domain name eg: google.com and wordlist.txt must be present in same directory
"""

import requests
import sys 

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for dir in directories:
	dir_enum = f"https://{sys.argv[1]}/{dir}.html"
	r = requests.get(dir_enum)
	if r.status_code == 404:
		pass 
	else:
		print("Valid directory: ", dir_enum)
