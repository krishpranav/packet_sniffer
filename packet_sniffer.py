import scapy.all as scapy
from scapy.layers import http
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="interface", help="Interface of the network (ex: enO / ethO)")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[!] Please add an interface to proceed, --help for more informations.")
    return options
 
 
