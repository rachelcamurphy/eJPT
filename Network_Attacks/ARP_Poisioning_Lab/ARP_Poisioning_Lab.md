#ARP Poisioning Lab - RCM 8/17/2021

#Description
In this lab you are connected to a switched network. Try to intercept network traffic and steal telnet credentials by performing an ARP poisioning attack.

#Goals
- Identify telnet server and the client machine
- intercept traffic between the two
- analyze the traffic and steal valid credentials
- login into the telnet server

#Tools
- Linux machine
- arpspoof
- Wireshark

Discovered 10.100.13.36,37,140 hosts up on the network.

Nmap scan report for 10.100.13.37 <-- telnet server
Nmap scan report for 10.100.13.36 <--client machine
Host is up (0.036s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
MAC Address: 00:50:56:A2:B1:3A (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 10.100.13.37
Host is up (0.036s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
23/tcp open  telnet  Linux telnetd
MAC Address: 00:50:56:A2:83:D4 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Performing an nmap service scan.
22/tcp open  ssh     OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
23/tcp open  telnet  Linux telnetd

`echo 1 > /proc/sys/net/ipv4/ip_forward`
