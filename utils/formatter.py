def process_and_save(findings, output_file="results.txt"):
    """
    Deduplicates results and sorts them by criticality.
    Formatting:
    - [!] CRITICAL: <url>
    - [+] MEDIUM: <url>
    - [-] LOW: <url>
    """
    # Simple deduplication
    unique_findings = list(set(findings))
    
    # Simple classification logic for demonstration
    # In reality, this would be based on response headers/content
    classified = []
    for item in unique_findings:
        if "admin" in item or "config" in item:
            classified.append(f"[!] CRITICAL: {item}")
        elif "api" in item:
            classified.append(f"[+] MEDIUM: {item}")
        else:
            classified.append(f"[-] LOW: {item}")
            
    with open(output_file, "w") as f:
        for entry in classified:
            f.write(entry + "\n")
            
    return classified
