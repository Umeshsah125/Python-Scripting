"""
Simple python script which take wordlist from the user and check whether the subdomains are valid or not
Condition Required are - Wordlist.txt should be present and domain should be provided as first argument
"""

import requests
import sys

sub_list = open("wordlist.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
	sub_domains = f"http://{sub}.{sys.argv[1]}"

	try:
		requests.get(sub_domains)

	except requests.ConnectionError:
		pass 

	else:
		print("Valid domain: ", sub_domains)
