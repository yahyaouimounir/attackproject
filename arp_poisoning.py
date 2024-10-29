import scapy.all as scapy

# Set the target IP address and MAC address
target_ip = "192.168.1.100"
target_mac = "00:11:22:33:44:55"

# Set the attacker's IP address and MAC address
attacker_ip = "192.168.1.200"
attacker_mac = "66:77:88:99:aa:bb"

# Create an ARP packet with the target's IP address and the attacker's MAC address
arp_packet = scapy.ARP(op=1, pdst=target_ip, hwdst=target_mac, psrc=attacker_ip, hwsrc=attacker_mac)

# Send the ARP packet to the target
scapy.sendp(arp_packet, iface="eth0", verbose=0)

print("ARP packet sent to", target_ip)