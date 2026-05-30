def display_banner():
    banner = """
    =================================================
    TwilightHawkEye - Advanced Reconnaissance Tool
    Created by: TwilightRaaz
    =================================================
    """
    print(banner)

def get_user_input():
    target = input("[?] Enter target IP or website: ")
    output_filename = input("[?] Enter output filename (saved in output/ folder): ")
    print("[?] Select Scan Impact Level:")
    print("    1. Low (Passive)")
    print("    2. Medium (Light Active)")
    print("    3. High (Heavy Active)")
    print("    4. Aggressive (Total Recon)")
    impact_choice = input("[?] Selection (1-4): ")
    
    impact_levels = {"1": "low", "2": "medium", "3": "high", "4": "aggressive"}
    impact = impact_levels.get(impact_choice, "low")
    
    return target, output_filename, impact
