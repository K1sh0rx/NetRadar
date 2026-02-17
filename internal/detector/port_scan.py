from collections import defaultdict
from internal.alerts.alert_manager import raise_alert

connection_count = defaultdict(int)

def detect_port_scan(src, dst):

    connection_count[src] += 1

    if connection_count[src] > 5:
        raise_alert(f"Possible Port Scan from {src}")
