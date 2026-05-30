import requests

def scan_api_endpoints(domain):
    """
    A basic API endpoint discovery implementation.
    Checks for common API paths.
    """
    print(f"[*] Starting API endpoint scan on {domain}...")
    
    # Common API paths to probe
    api_paths = ["/api/v1", "/api/v2", "/graphql", "/swagger.json", "/v1"]
    found = []
    
    for path in api_paths:
        url = f"https://{domain}{path}"
        try:
            # We check if the path exists or returns something interesting
            response = requests.get(url, timeout=2)
            if response.status_code in [200, 403, 401]:
                print(f"[+] Possible API endpoint found: {url} (Status: {response.status_code})")
                found.append(url)
        except requests.RequestException:
            pass
            
    return found
