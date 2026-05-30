import requests

def brute_force_directories(domain, wordlist=None):
    """
    A basic directory brute-forcing implementation.
    In a production tool, this would use a robust wordlist.
    """
    print(f"[*] Starting directory brute-forcing on {domain}...")
    
    # Simple wordlist for demonstration
    if not wordlist:
        wordlist = ["admin", "login", "config", "backup", "api"]
    
    found = []
    for directory in wordlist:
        url = f"https://{domain}/{directory}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
                found.append(url)
        except requests.RequestException:
            pass
    return found
