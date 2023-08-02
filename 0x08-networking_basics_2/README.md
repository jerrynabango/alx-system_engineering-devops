# localhost: It refers to the local device or computer used to access itself. It is a standard hostname that resolves to the loopback network interface, which is typically assigned the IP address 127.0.0.1 in IPv4 or ::1 in IPv6.

# 0.0.0.0: It is not assigned to any specific device but rather represents a non-routable meta-address used for different purposes, depending on the context in which it is used. The following is a list of it's functions:

1. Broadcast Address: Responsible for broadcasting address within a local network segment. When an application sends data to the broadcast address, it will be received by all devices on the same network.

2. Bind to All Interfaces: During server configurations, when a service is set to listen on "0.0.0.0," it means that the service will bind to all available network interfaces on the device. This allows the service to listen for incoming connections from any interface either Ethernet or  Wi-Fi that the device supports.

3. Default Route: Works as a default route, also known as default gateway. It indicates that any traffic with an unknown destination should be sent to this route. In other words, it serves as a catch-all for traffic not destined for any specific network.

4. Unspecified Address: It shows that an IP address has not been assigned to the device or that it is used when a specific IP address is not required for a particular setting.

* "0.0.0.0" is not a valid address for identifying the specific device on a network, and it should not be used for regular communication between devices. It's a reserved address with special meaning, used for specific networking purposes.

# host file: lain text file found in most operating systems that maps hostnames to IP addresses. It acts as a local domain name system (DNS) resolver and is used to override DNS resolution for specific hostnames on the local device.

* One can manually associate IP addresses with the hostnames, effectively bypassing the need to query DNS server when resolving domain names to IP addresses.

# Netcat: versatile networking utility used to establish and manage network connections. Also referred to as "swiss army knife" of networking due to its wide range of functionalities.
