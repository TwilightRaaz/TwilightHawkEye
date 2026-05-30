import sys
import os
from utils.interactive import display_banner, get_user_input
from modules.engine import run_recon

def main():
    display_banner()
    target, filename, impact = get_user_input()
    
    output_path = os.path.join("output", filename)
    print(f"[*] Reconnaissance target: {target}")
    print(f"[*] Impact level selected: {impact.upper()}")
    print(f"[*] Findings will be saved to: {output_path}")
    
    print(f"[*] Starting reconnaissance sequence at {impact} level...")
    run_recon(target, output_path, impact)

if __name__ == "__main__":
    main()
