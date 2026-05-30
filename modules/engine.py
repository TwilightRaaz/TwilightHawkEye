import subprocess
import os
from utils.formatter import process_and_save

def run_tool(command):
    print(f"[*] Running: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running command: {e}")

def run_recon(target, output_path, impact):
    # Base tools (always run)
    subdomains_file = "subdomains.txt"
    run_tool(["subfinder", "-d", target, "-o", subdomains_file])
    
    findings = []
    if os.path.exists(subdomains_file):
        with open(subdomains_file, 'r') as f:
            findings.extend(f.read().splitlines())
    
    if impact in ["medium", "high", "aggressive"]:
        run_tool(["httpx", "-l", subdomains_file, "-o", output_path + "_httpx.txt"])
        if os.path.exists(output_path + "_httpx.txt"):
            with open(output_path + "_httpx.txt", 'r') as f:
                findings.extend(f.read().splitlines())
    
    if impact in ["high", "aggressive"]:
        run_tool(["naabu", "-l", subdomains_file, "-o", output_path + "_ports.txt"])
        run_tool(["katana", "-u", target, "-o", output_path + "_crawl.txt"])
        
    if impact == "aggressive":
        run_tool(["nmap", "-sV", target, "-oN", output_path + "_nmap.txt"])
        run_tool(["feroxbuster", "-u", f"https://{target}", "-o", output_path + "_dirs.txt"])
        run_tool(["nuclei", "-target", target, "-o", output_path + "_vulns.txt"])

    # Final processing and saving
    print(f"[*] Processing all findings for {target}...")
    final_output = output_path + "_final_report.txt"
    process_and_save(findings, final_output)

    print(f"[*] Reconnaissance complete. Findings saved in {final_output}")
