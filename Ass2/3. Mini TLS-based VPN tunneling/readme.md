# Attacking and defending networks

## 3. Mini TLS-based VPN tunneling

For this part, less familiarity with low-level networking programming details is necessary. In particular, this [SEED lab](https://seedsecuritylabs.org/Labs_16.04/Networking/VPN_Tunnel/) has starting code for reference.
The objective of this task is to implement a small VPN tunneling program that will allow hosts to communicate over an encrypted connection. Follow the tutorial from the SEED lab above (while ignoring the instructions to write a report) until you have a functional implementation able to transmit unencrypted traffic. Your task is then to finalize the implementation by replacing the UDP socket with a TLS/SSL connection. A simple certificate structure must be deployed, where a self-signed certificate will authenticate the server certificate and be available on the client side as well.
Collect evidence of the correct behavior through Wireshark and screenshots showing that traffic is correctly forwarded.
