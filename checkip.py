import requests
import sys

API_KEY = 'YOUR_API_KEY'  # Replace with your AbuseIPDB API key

def check_ip_reputation(ip_address):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {'Key': API_KEY, 'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        ip = data['data']['ipAddress']
        reputation_score = data['data']['abuseConfidenceScore']
        host = data['data']['host']
        reported_abuses = data['data']['totalReports']
        
        print(f"IP Address: {ip}")
        print(f"Reputation Score: {reputation_score}")
        print(f"Host: {host}")
        print(f"Reported Abuses: {reported_abuses}")
        
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
        print("Usage: python3 check_ip_reputation.py <IP_ADDRESS>")
    else:
        ip_address = sys.argv[1]
        if not validate_ip_address(ip_address):
            print("Please provide a valid IP address as the argument.")
        else:
            check_ip_reputation(ip_address)

if __name__ == '__main__':
    main()
