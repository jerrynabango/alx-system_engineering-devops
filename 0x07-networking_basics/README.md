# OSI stands for Open Systems Interconnection. It is a conceptual framework that standardizes functions of a telecommunication or computing system into seven distinct layers.
* The seven layers of the OSI model, from the highest are:

1. Application Layer: Provides network services directly to the user or application. It deals with protocols and processes related to applications, such as web browsers, email clients, and file transfer applications.

2. Presentation Layer: Responsible for data translation, compression, and encryption, ensuring that data from the application layer of one system can be understood by the application layer of another system.

3. Session Layer: It establishes, maintains, and terminates connections between applications. It manages the communication sessions, which are logical connections between two systems.

4. Transport Layer: Responsible for end-to-end communication between hosts. It ensures reliable and error-checked data delivery and provides flow control, segmentation, and reassembly of data.

5. Network Layer: Responsible for routing and forwarding data packets across multiple networks. It determines the best path for data transmission between source and destination hosts.

6. Data Link Layer: Responsible for reliable data transfer between two directly connected devices on the same network. It handles framing, physical addressing, and error detection.

7. Physical Layer: Responsible for the physical medium over which data is transmitted. It specifies the hardware, cabling, and signaling used to transmit raw bits over a network.

# The OSI model serves as the conceptual guide for designing and implementing network protocols and communication systems.

# ICMP stands for "Internet Control Message Protocol." It's an essential protocol in Internet Protocol Suite and is primarily used for the diagnostic and control purposes in IP networks. ICMP operates at the network layer (Layer 3) of the OSI model.

* The main functions of ICMP include:

1. Error Reporting: ICMP is used to report errors related to network communications. For example, when a router encounters an issue forwarding an IP packet, it can send an ICMP error message back to the source of the packet, informing it of the problem.

2. Network Reachability Testing: The most common use of ICMP is for network reachability testing, which is achieved through the "ping" command. When you ping a network host, your computer sends ICMP echo request packets to the destination, and if the destination host is reachable and operational, it responds with ICMP echo reply packets.

3. Echo and Echo Reply: ICMP echo request and reply messages are used in ping process. They help determine whether a host is online and how long it takes for a packet to travel from the source to the destination.
4. Path MTU Discovery: ICMP helps discover Maximum Transmission Unit (MTU) along a path between two hosts. Also helps determine maximum size of packets that can be transmitted without fragmentation.

5. Redirect Messages: ICMP redirect messages are used by routers to inform hosts about more efficient routes to the specific destinations.

6. Time Exceeded: ICMP time exceeded messages are sent when a packet's time-to-live (TTL) reaches zero or when a fragment is discarded due to an exceeded hop limit.
Redirect Messages: ICMP redirect messages are used by routers to inform hosts about more efficient routes to the specific destinations.

7. Echo and Echo Reply: ICMP echo request and reply messages are used in ping process. They help determine whether a host is online and how long it takes for a packet to travel from the source to the destination.

# TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the most common transport layer protocols in the Internet Protocol Suite (TCP/IP). They are responsible for facilitating communication between applications running on different devices over a network

* The differences include:
1. Connection-Oriented vs. Connectionless:

* TCP is a connection-oriented protocol, it establishes a reliable and dedicated connection before data transmission. It involves a three-way handshake process (SYN, SYN-ACK, ACK) to set up connection. Once the connection is established, data is sent in a stream, and the receiver acknowledges the receipt of each data packet. If a packet is lost, TCP retransmits it ensuring reliable data delivery.
UDP is a connectionless protocol, meaning it does not establish dedicated connection before sending data. Each UDP packet is independent, and there is no handshake process. UDP is considered "best-effort," as it does not guarantee reliable delivery or packet order. It simply sends packets without checking if they are received.

2. Reliability and Handling error:

* TCP provides reliable data delivery. It ensures data packets are delivered to the destination in the correct order and without loss or duplication. If any packet is lost or corrupted during transmission, TCP requests retransmission ensuring complete and error-free data delivery.
UDP does not guarantee reliability or error checking. If packets are lost or corrupted during transmission, UDP does not request retransmission, and the application must handle any necessary error recovery.

3. Overhead and Efficiency:

TCP has a higher overhead due to the additional mechanisms for establishing and maintaining connections, managing sequence numbers, and ensuring reliable delivery. This can lead to more substantial network traffic.
UDP has lower overhead, as it does not require connection setup and teardown. It has a smaller packet header, making it more efficient for certain types of data transmission.

4. Use Cases:

* TCP is suitable for applications that require reliable, ordered, and error-checked data delivery, such as web browsing, email, file transfer, and most client-server communication scenarios.
UDP is used in applications where low latency and minimal overhead are crucial, even if it means sacrificing reliability. Common uses of UDP include real-time audio and video streaming, online gaming, DNS (Domain Name System) queries, and other time-sensitive applications.

5. Ordering:

* TCP guarantees that data is received in the same order it was sent. It maintains the correct sequence of data packets.
UDP does not guarantee the order of data delivery. Packets may arrive at the destination out of order.
* TCP provides more reliable, ordered, and connection-oriented communication, compared to UDP which offers lower overhead, connectionless communication, and faster data transmission but without the guarantees of reliability and ordering. The choice between TCP and UDP depends on the specific requirements and characteristics of the application or service being developed or used.

# Media Access Control. It is a unique identifier assigned to a network interface controller (NIC) or network adapter. The MAC address is a hardware address that is hardcoded into the network interface during manufacturing and serves as a permanent and globally unique identifier for that particular device.

* It's assigned to devices at Data Link Layer (Layer 2) of the OSI model. The Data Link Layer is responsible for providing reliable link between two directly connected nodes over a physical network medium.

* A MAC address is a 48-bit address, represented in a hexadecimal format, displayed in the following format: XX:XX:XX:XX:XX:XX. Each pair of XX represents one byte (8 bits) of the address. First 24 bits (6 hexadecimal characters) represent the organizationally unique identifier (OUI), which is assigned to a specific manufacturer by the IEEE (Institute of Electrical and Electronics Engineers). The last 24 bits (6 hexadecimal characters) represent the unique identifier assigned by the manufacturer to the specific network interface.

* All network device with a network adapter. This uniqueness makes it possible for devices to communicate over the same local network without conflict.

* MAC addresses are primarily used at the Data Link Layer for local network communication, such as Ethernet LANs. When data is sent between devices on the same local network, the data frames are addressed to the destination MAC address to ensure that the correct device receives the data. On the internet, however, devices use IP (Internet Protocol) addresses for global communication.

* MAC addresses and IP addresses, perform different functions and operate at different layers of the network stack.
# IP addresses are used for global routing on the internet, while MAC addresses are used for local data link layer communication on a specific network segment.

* Used at Network Layer (Layer 3) of the OSI model and are part of the TCP/IP protocol suite. There are two primary versions of IP addresses in use today:

1. IPv4 (Internet Protocol version 4): IPv4 addresses are 32-bit binary numbers, usually represented in decimal format as four sets of numbers separated by dots. Each number represents 8 bits, and the range of each set is from 0 to 255. For example: 192.168.1.1.

2. IPv6 (Internet Protocol version 6): IPv6 addresses are 128-bit binary numbers, represented in hexadecimal format as eight sets of four hexadecimal digits separated by colons. IPv6 was introduced to address the depletion of available IPv4 addresses and to accommodate the growing number of devices connected to the internet. For example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.

IP addresses serve several essential functions:

* Network Segmentation: Responsible for the division of large networks into smaller subnetworks, providing better network management and improved security.

* Addressing: Responsible for uniquely identifying each device on the network. It allows data packets to be correctly routed from main source to the destination.

* Internet Connectivity: Responsible for communication between devices across the global internet.

* Routing: Routers use IP addresses to determine best path for data packets to reach their destination across interconnected networks.
