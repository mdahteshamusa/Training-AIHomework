import requests
import sys
#response = requests.get("https://api.macaddress.io/v1?apiKey=at_PYc61TXP4CpeJ05erBj80UeF2bH6H&output=json&search=44:38:39:ff:ef:57")
#print(response.json()['vendorDetails'].get('companyName'))


def get_req():
	try:
		macad='44:38:39:ff:ef:57'
		PARAMS = {'search': macad}
		response = requests.get("https://api.macaddress.io/v1?apiKey=at_PYc61TXP4CpeJ05erBj80UeF2bH6H&output=json",params=PARAMS)	
		response.raise_for_status()
		response_json=response.json()
		response_company_name=response_json['vendorDetails'].get('companyName')
		return response_company_name
	except requests.exceptions.HTTPError as error:
		
		return error
	
output=get_req()
print(output)