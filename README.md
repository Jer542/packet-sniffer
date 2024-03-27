# Packet Sniffer

This is a simple packet sniffer written in Python. It uses raw sockets to listen for IP packets and logs the protocol, source IP address, and destination IP address of each packet.

## Requirements

- Python 3.x
- Windows or Unix-based system

## Usage

1. Run the packetsniffer.py script with administrator privileges (required for using raw sockets). On Windows, you can do this by right-clicking on the Command Prompt and selecting "Run as administrator". On Unix-based systems, use the `sudo` command. Ensure ip_header.py is in the same directory or you modify the import in packetsniffer.py

2. The script will start listening for IP packets and log the protocol, source IP address, and destination IP address of each packet.

3. To stop the script, press `Ctrl+C`.

## Code Structure

- `get_host_ip()`: This function gets the IP address of the host machine.

- `create_socket(host)`: This function creates a raw socket, binds it to the host, and sets the necessary socket options.

- `main()`: This is the main function of the script. It gets the host IP, creates a socket, and starts listening for packets. When a packet is received, it extracts the IP header and logs the protocol, source IP address, and destination IP address.

## Note

Due to the use of raw sockets, this script may not work on some networks or machines due to restrictions and permissions.
