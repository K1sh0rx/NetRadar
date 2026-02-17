from internal.detector.port_scan import detect_port_scan

def parse_packet(packet):

    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst

        print(f"[Packet] {src} -> {dst}")

        detect_port_scan(src, dst)
