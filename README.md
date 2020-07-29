# packet_sniffer
This tool will sniff http packets in your network 
NOTE THIS TOOL WILL SNIFF HTTP PACKETS ONLY NOT HTTPS 

steps to use this tool:
   1. git clone https://github.com/krishpranav/packet_sniffer
   2. cd packet_sniffer
   3. sudo chmod 777 *
   4. python3 -m pip install -r requirements.txt
   5. python packet_sniffer.py

NOTE: change your interface in the line 24 sniff("en1") i gave as en1 you want to put your interface 
to bypass https 
USE THESE COMMANDS:
    1. use arp_spoofer before running this tool
    2. ssl strip
    3. iptables -t net -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
    link for arp spoofer git clone https://github.com/krishpranav/arp_spoofer

CREATED BY KRISHNA PRANAV
