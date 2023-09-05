#!/usr/bin/python3

import config

import requests
import sys
import json

API_KEY = config.abuseipdb_api_key

def check_ip_reputation(ip_address):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {'Key': API_KEY, 'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        initialapidata = response.json()

        # Replace single quotes with double quotes to make this valid JSON
        # apidata = initialapidata.replace("'", "\"")
        apidata = json.dumps(initialapidata, indent=4, sort_keys=True)

        # Step 1: Parse the JSON data into a Python dictionary
        apidata_dict = json.loads(apidata)

        # Step 2: Convert the dictionary into a list of tuples
        apidata_tuple_list = [(key, value) for key, value in apidata_dict['data'].items()]
        #       tuple_list = [(key, value) for key, value in data['data'].items()]

        print(apidata_tuple_list)

        # Find the maximum width for each column
        max_widths = [max(len(str(item)) for item in column) for column in zip(*apidata_tuple_list)]

        # Create a format string based on column widths
        format_string = " | ".join(f"{{:<{width}}}" for width in max_widths)

        # Print the table header
        # print(format_string.format(*apidata_tuple_list[0]))

        # Print the data rows
        # for row in apidata_tuple_list[1:]:
        #    print(format_string.format(*row))

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")

def validate_ip_address(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) > 255:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 checkip.py <IP_ADDRESS>")
    else:
        ip_address = sys.argv[1]
        if not validate_ip_address(ip_address):
            print("Please provide a valid IP address as the argument.")
        else:
            check_ip_reputation(ip_address)

if __name__ == '__main__':
    main()