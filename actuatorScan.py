import requests
import sys

# Actuator端点列表
endpoints = [
    "/actuator", "/actuator/health", "/actuator/info",
    "/actuator/env", "/actuator/metrics", "/actuator/logfile"
]

def check_vulnerability(url):
    for endpoint in endpoints:
        full_url = f"{url}{endpoint}"
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Vulnerable endpoint found: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {full_url}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 actuatorScan.py <urls_file>")
        sys.exit(1)
    
    urls_file = sys.argv[1]
    with open(urls_file, "r") as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()
        if url:
            print(f"[*] Checking {url}")
            check_vulnerability(url)
