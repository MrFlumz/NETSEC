from collections import Counter
from scapy.all import sniff
from scapy.interfaces import show_interfaces

## Create a Packet Counter
packet_counts = Counter()

## Define our Custom Action function
def custom_action(packet):
    # Create tuple of Src/Dst in sorted order
    print(bytes(packet).decode('latin-1'))
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    return f"Packet #{sum(packet_counts.values())}: {packet[0][1].src} ==> {packet[0][1].dst}"

## Setup sniff, filtering for IP traffic
#print(show_interfaces())

sniff(filter="ip and host 127.0.0.1 and port 50656",iface="lo", prn=custom_action, count=100)

## Print out packet count per A <--> Z address pair
#print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))