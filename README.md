# TwilightHawkEye

TwilightHawkEye is an advanced, automated reconnaissance tool designed for bug bounty hunters and cybersecurity professionals. It orchestrates powerful security tools to perform structured, productive, and efficient reconnaissance.

**Created by: TwilightRaaz**

---

## Features
- **Reconnaissance:** Subdomain enumeration (Subfinder).
- **Active Probing:** DNS resolution and HTTP probing (Httpx, DnsX).
- **Scanning:** Port scanning (Naabu, Nmap) and web directory discovery (Feroxbuster).
- **Vulnerability Assessment:** Automated vulnerability scanning (Nuclei).
- **Crawling:** Web crawling and endpoint discovery (Katana).
- **Intelligence:** Data deduplication, criticality-based classification, and professional reporting.

---

## Installation

TwilightHawkEye requires Go and several security tools to function.

1. **Install Dependencies (Termux/Linux):**
   ```bash
   pkg install -y golang nmap feroxbuster
   ```

2. **Install ProjectDiscovery Tools:**
   ```bash
   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
   go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
   go install -v github.com/projectdiscovery/katana/cmd/katana@latest
   go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
   go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
   ```

3. **Ensure Path Configuration:**
   Add `$(go env GOPATH)/bin` to your system PATH.

---

## Usage

Run the tool using the command:
```bash
python3 main.py
```

### Interactive Flow
1. Enter the **Target** (domain or IP).
2. Specify the **Output Filename**.
3. Select the **Impact Level**:
   - **1. Low (Passive):** Quick, silent reconnaissance. Best for initial scope discovery.
   - **2. Medium (Light Active):** Adds active HTTP probing. Use for verifying alive domains.
   - **3. High (Heavy Active):** Adds deep scanning and crawling. Use when you have explicit testing permission.
   - **4. Aggressive (Total Recon):** Full suite of Nmap, directory brute-forcing, and vulnerability scanning. Use for comprehensive deep-dive security assessments.

All results will be processed, deduplicated, and classified in the `output/` folder as `[filename]_final_report.txt`.

---

## When to use this
- **Bug Bounty:** To automate the initial reconnaissance phase of your methodology.
- **Security Auditing:** To quickly map an organization's external attack surface.
- **CTF/Practice:** To practice reconnaissance workflows against authorized targets.

*Always ensure you have explicit written permission before scanning any target.*
