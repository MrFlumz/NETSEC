# Attacking and defending networks

## 1. Encrypted covert channel

For this part, you will need to have some familiarity with the IP protocol to write low-level networking code using a library. Suggestions are the `libnet/libpcap` library in the C programming language or the equivalent `socket` package in Python.

The objective of this task is to to implement an encrypted covert channel using the [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) (Internet Control Message Protocol) protocol. ICMP is an error-reporting protocol that network devices use to inform of error messages to the source IP address when network problems prevent an IP packet to be delivered.
The most familiar contact we have with the ICMP protocol is the `ping` tool using the `Echo Request` and `Echo Reply` messages. While these packets are typically small, it is not well-known that ICMP packets can carry much larger pieces of data.

You will implement client/server programs to exchange encrypted covert channel through the network. For this, use ICMP messages with code `47`. The client program should receive a destination IP address to transmit and wait for input in the client. The server program should listen the network for such messages and print them in the console as they arrive. For encryption, you are free to use a preshared symmetric key to protect the transmitted payload. Choose algorithms and modes of operation wisely.
