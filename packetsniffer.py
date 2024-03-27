import socket
import os
import logging
from ip_header import IP

# Constants
BUFFER_SIZE = 65565
IP_HEADER_SIZE = 20
logging.basicConfig(level=logging.INFO)

def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except socket.gaierror:
        logging.error("Unable to get Hostname and IP")
        return None

def create_socket(host):
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    return sniffer

def main():
    host = get_host_ip()
    sniffer = create_socket(host)
    try:
        while True:
            raw_buffer = sniffer.recvfrom(BUFFER_SIZE)[0]
            ip_header = IP(raw_buffer[0:IP_HEADER_SIZE])
            logging.info("Protocol: %s %s -> %s", ip_header.protocol, ip_header.src_address, ip_header.dst_address)
    except KeyboardInterrupt:
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    main()