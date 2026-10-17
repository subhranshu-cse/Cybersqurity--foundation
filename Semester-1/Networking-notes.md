# Computer Networking

> Complete Notes — Basic to Advanced  
> Language: Simple English  
> Includes: Diagrams, Examples, Practice Sets and Revision

---

## 1. Introduction to Computer Networking

A **computer network** is a system in which two or more devices are connected so they can communicate and share data, resources, and services.

A network may contain:

- Computers
- Smartphones
- Printers
- Servers
- Switches
- Routers
- Wireless devices

### Basic Network Diagram

```text
Computer A
     |
   Switch
     |
Computer B
     |
   Router
     |
  Internet





## Day 2 — Types of Networks

### PAN (Personal Area Network)
A small network around one person.

### LAN (Local Area Network)
A network within a home, room, laboratory, office, or building.

### MAN (Metropolitan Area Network)
A network covering a city or large metropolitan area.

### WAN (Wide Area Network)
A network covering a large geographic area.
The Internet is a major example.

### Quick Revision

PAN → Personal devices  
LAN → Home / Office / Lab  
MAN → City  
WAN → Large geographic area

### Practice Set

1. Which network connects personal devices?
2. Which network is common in an office?
3. Which type covers the largest area?

### Answers


1. PAN
2. LAN
3. WAN


---

## Day 3 — OSI & TCP/IP Models

### OSI Model

The OSI (Open Systems Interconnection) Model has 7 layers:

1. Application
2. Presentation
3. Session
4. Transport
5. Network
6. Data Link
7. Physical

### TCP/IP Model

The TCP/IP Model is commonly divided into 4 layers:

1. Application
2. Transport
3. Internet
4. Network Access

### Important Concepts

- IP address works at OSI Layer 3 — Network Layer.
- TCP and UDP work at OSI Layer 4 — Transport Layer.
- Port numbers are used at the Transport Layer to identify services/applications.
- TCP is connection-oriented and provides reliable data delivery.
- UDP is connectionless and does not guarantee delivery.

### Important Questions & Answers

**Q1. Which OSI layer uses IP?**

**Answer:** Layer 3 — Network Layer.

**Q2. Which OSI layer uses TCP/UDP and ports?**

**Answer:** Layer 4 — Transport Layer.

**Q3. How many layers are in the OSI Model?**

**Answer:** 7 layers.

**Q4. How many layers are commonly used in the TCP/IP Model?**

**Answer:** 4 layers.

**Q5. What is the main purpose of the Transport Layer?**

**Answer:** It provides end-to-end communication using protocols such as TCP and UDP and uses port numbers to identify applications.

### Easy Memory Trick

**OSI:**  
All People Seem To Need Data Processing

**TCP/IP:**  
Application → Transport → Internet → Network Access


# 📘 Networking Day 4 — Network Devices

## 1. What are Network Devices?

Network devices are hardware devices used to connect computers and other devices so they can communicate and share data.

Examples:
- Hub
- Switch
- Router
- Modem
- Access Point
- Repeater
- Bridge
- Firewall

---

## 2. Hub

A Hub connects multiple devices in a network.

### How it works:
When a hub receives data, it sends the data to ALL connected devices.

Example:

PC1 → Hub → PC2
          ↓
        PC3
          ↓
        PC4

⚠️ Problem:
- Sends data to everyone
- More network traffic
- Less secure
- Works mainly at OSI Layer 1 (Physical Layer)

---

## 3. Switch

A Switch connects devices in a LAN.

Unlike a hub, a switch sends data only to the correct destination device.

Example:

PC1 → Switch → PC2
               ↓
              PC3

If PC1 wants to communicate with PC2, the switch forwards the frame to PC2.

### Important:
- Uses MAC Address
- Works mainly at OSI Layer 2 (Data Link Layer)
- Reduces unnecessary traffic
- More efficient than a Hub

---

## 4. Router

A Router connects different networks.

Example:

Computer Network → Router → Internet

A router uses IP addresses to decide where packets should go.

### Important:
- Uses IP Address
- Works mainly at OSI Layer 3 (Network Layer)
- Connects different networks
- Can provide routing and NAT

---

## 5. Modem

Modem stands for:

Modulator + Demodulator

It converts signals so that devices can communicate with an Internet Service Provider (ISP).

Simple flow:

Home Network → Modem → ISP → Internet

---

## 6. Access Point (AP)

An Access Point allows wireless devices to connect to a wired network using Wi-Fi.

Example:

Laptop ))))
          ↓
       Access Point
          ↓
       Switch/Router
          ↓
       Internet

Used in:
- Offices
- Colleges
- Homes
- Hotels

---

## 7. Repeater

A Repeater receives a weak signal and regenerates it to extend the network range.

Example:

Router →→→ Weak Signal → Repeater →→→ Stronger Signal

### Purpose:
To increase network coverage.

---

## 8. Bridge

A Bridge connects two network segments and helps control traffic between them.

Example:

LAN 1 → Bridge → LAN 2

A bridge works mainly at OSI Layer 2.

---

## 9. Firewall

A Firewall controls incoming and outgoing network traffic based on security rules.

Example:

Internet → Firewall → Computer

It can:
✅ Allow trusted traffic
❌ Block unauthorized traffic

### Practical Example:

If a firewall blocks TCP port 23, Telnet traffic may be prevented.

Firewalls are very important in Cyber Security and SOC environments.

---

# 🔥 Hub vs Switch vs Router

| Device | Main Address | Main Function | OSI Layer |
|--------|--------------|---------------|-----------|
| Hub | None | Sends data to all ports | Layer 1 |
| Switch | MAC Address | Sends data to destination device | Layer 2 |
| Router | IP Address | Connects different networks | Layer 3 |

---

# 🛠️ Practical Commands

### Windows

Check network information:

```bash
ipconfig




Day 5: IP Address vs MAC Address

1. What is an IP Address?

An IP (Internet Protocol) address is a logical address assigned to a device on a network.

Purpose: It helps identify a device's network location and enables communication between networks.

Example: "192.168.1.10"

Types:

- IPv4
- IPv6

2. What is a MAC Address?

A MAC (Media Access Control) address is a hardware address associated with a network interface.

Purpose: It identifies a network interface for communication within a local network.

Example: "A4:5E:60:C2:10:9B"

3. Difference Between IP Address and MAC Address

IP Address| MAC Address
Logical address| Hardware address
Works at the Network Layer (Layer 3)| Works at the Data Link Layer (Layer 2)
Can change depending on the network| Usually assigned to the network interface
Used for routing between networks| Used for delivery within a local network
IPv4 and IPv6 are common versions| Commonly represented as 48 bits

4. Example

Suppose your laptop connects to a Wi-Fi network.

- IP Address: "192.168.1.10"
- MAC Address: "A4:5E:60:C2:10:9B"

The IP address helps identify your device's network location, while the MAC address helps deliver Ethernet or Wi-Fi frames over the local network.

Note: These are example addresses, not your actual device addresses.

5. Why Is This Important in Cybersecurity?

Understanding IP and MAC addresses helps with:

- Network troubleshooting
- Packet analysis using Wireshark
- Understanding ARP
- Investigating suspicious network activity
- Learning network security fundamentals

6. Practical Commands

Windows CMD:

ipconfig

Displays IP configuration.

ipconfig /all

Displays detailed network information, including the physical address.

arp -a

Displays the ARP cache, which maps known IPv4 addresses to MAC addresses on the local network.

7. Quick Revision

- IP Address = Logical address
- MAC Address = Hardware address associated with a network interface
- ARP = Resolves IPv4 addresses to MAC addresses on a local network
- IPv4 = 32 bits
- IPv6 = 128 bits
- Traditional MAC address = 48 bits

Conclusion

IP addresses help identify network locations, while MAC addresses help deliver frames across a local network. Both are important foundations for networking and cybersecurity.
Day 6: Static IP Address

1. What is a Static IP Address?

A Static IP address is an IP address that remains the same until it is manually changed or its configuration is modified.

It can be configured manually on a device or reserved for that device through DHCP.

2. Example

IP Address: "192.168.1.10"

Subnet Mask: "255.255.255.0"

Default Gateway: "192.168.1.1"

DNS Server: "8.8.8.8"

These are example network settings.

3. Advantages of Static IP

- Provides a consistent IP address.
- Useful for servers and network devices.
- Makes remote access easier.
- Helps configure firewall rules.

4. Disadvantages of Static IP

- Requires proper configuration.
- Incorrect settings can cause network problems.
- Duplicate IP addresses can cause conflicts.

5. Uses of Static IP

- Web servers
- DNS servers
- Network printers
- Network infrastructure

6. Practical (Windows CMD)

To check your current IP configuration, use:

ipconfig

To view detailed network information, use:

ipconfig /all

Note: These commands display your current configuration; they do not set a Static IP address.

Conclusion

A Static IP address provides consistent addressing and is useful for servers and network devices that need a predictable IP address.



Day 7: Dynamic IP Address

1. What is a Dynamic IP Address?

A Dynamic IP address is an IP address assigned automatically to a device by a DHCP (Dynamic Host Configuration Protocol) server.

The IP address may change over time depending on the network configuration and DHCP lease.

2. Example

IP Address: "192.168.1.15"

Subnet Mask: "255.255.255.0"

Default Gateway: "192.168.1.1"

DNS Server: "8.8.8.8"

These are example network settings assigned to a device.

3. Advantages of Dynamic IP

- Automatically assigns IP addresses.
- Reduces manual configuration.
- Makes network management easier.
- Helps prevent address conflicts when DHCP is configured correctly.

4. Disadvantages of Dynamic IP

- The IP address may change over time.
- Remote access can be more difficult if an address changes.
- DHCP problems can prevent devices from receiving valid network settings.

5. Uses of Dynamic IP

- Home Wi-Fi networks
- Office networks
- Smartphones
- Laptops
- Public Wi-Fi networks

6. Practical (Windows CMD)

To check your current IP configuration:

ipconfig

To view detailed network information:

ipconfig /all

To request an IPv4 address through DHCP:

ipconfig /renew

Note: The "/renew" command requests a renewed DHCP configuration. It does not guarantee that the IP address will change.

7. What is DHCP?

DHCP stands for Dynamic Host Configuration Protocol.

It automatically provides devices with network settings such as:

- IP address
- Subnet mask
- Default gateway
- DNS server

Conclusion

A Dynamic IP address is assigned automatically, usually through DHCP. It simplifies IP address management and is commonly used for laptops, smartphones, and other client devices.
