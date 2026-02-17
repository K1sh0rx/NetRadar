from scapy.all import sniff
from internal.parser.parser import parse_packet

def packet_callback(packet):
    parsed = parse_packet(packet)

def start_sniffing():
    sniff(prn=packet_callback, count=10)
