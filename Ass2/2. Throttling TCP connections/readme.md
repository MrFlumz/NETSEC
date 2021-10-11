# Attacking and defending networks

## 2. Throttling TCP connections

For this part, you will need to have some familiarity with the TCP protocol to write low-level networking code using a library. Suggestions again are the `libnet/libpcap` library in the C programming language or the equivalent `Scapy` package in Python.

The objective of this task is to slow down or interrupt TCP connections by forcing retransmission of packets. An illustrative example of such an approach is the `tcpnice` program in the `dsniff` package which reduces windows advertised to artificially decrease bandwidth. We will adopt two different approaches: send 3 ACK packets to simulate packet loss and force retransmission; send a TCP reset packet to drop the connection altogether. You will implement a tool that receives a source and destination IP addresses to listen for TCP connections and what approach should be used. Whenever such a packet is captured, 3 ACK packets or RST should be sent back to the origin and/or destination.
Collect experimental evidence of the malicious behavior through Wireshark and screenshots of the time taken to transmit a file using a file transfer (FTP or SSH) to show that it is indeed slower or interrupted when under attack.
