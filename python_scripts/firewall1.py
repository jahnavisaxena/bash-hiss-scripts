import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"
    
def check_firewall_rules(ip,rules):
    for rule_ip,action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
firewall_rules = {
        "192.168.1.1" : "BLOCK",
        "192.168.1.4" : "BLOCK",
        "192.168.1.9" : "BLOCK",
        "192.168.1.13" : "BLOCK",
        "192.168.1.16" : "BLOCK",
        "192.168.1.19" : "BLOC",
        
}
for_in range(12):
    ip_address = gernerate_random_ip()
    action = check_firewall_rules(ip_address,firewall_rules)
    random_number = random.randint(0,9999)
    print(f"IP:{ip_address},Action: {action}, Random: {random_number}")

if__name__="main":
    main()
    
