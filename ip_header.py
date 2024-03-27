from ctypes import *
import socket
import struct

class IP(Structure):
    """IP Class for parsing IP headers."""

    _fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        ("src", c_uint32),
        ("dst", c_uint32)
    ]

    # map protocol constants to their names
    protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

    def __new__(cls, socket_buffer=None):
        """Create a new IP object from a socket buffer."""
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        """Initialize the IP object."""
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except KeyError:
            self.protocol = str(self.protocol_num)