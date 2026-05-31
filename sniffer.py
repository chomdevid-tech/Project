from scapy.all import sniff
from scapy.layers.inet import IP, TCP
import queue

# Global queue for sending events to event_bridge
EVENT_QUEUE = queue.Queue()

FTP_PORT = 21
MYSQL_PORT = 3306


def push_event(event):
    # Push event to the global queue
    EVENT_QUEUE.put(event)


def process_packet(pkt):
    # Process each captured packet
    if not pkt.haslayer(IP) or not pkt.haslayer(TCP):
        return

    src = pkt[IP].src
    dst_port = pkt[TCP].dport
    flags = pkt[TCP].flags

    if dst_port in (FTP_PORT, MYSQL_PORT):
        push_event({"ip": src, "action": "login_fail"})

    #  SYN packet ONLY (flags = 0x02)
    if flags & 0x02: 
        push_event({
            "ip": src,
            "action": "scan",
            "port": dst_port
        })
        return

    push_event({"ip": src, "action": "request"})


def start_sniffer():
    print("[Sniffer] Started...")
    sniff(filter="tcp", prn=process_packet, store=0)
