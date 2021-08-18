#INE Scanning and OS Fingerprinting Lab.
#RCM 8/2021

#Goals
- Run ping scan with fping 
`fping -a -g 10.142.111.240/24 > ~/Desktop/INE/Scanning_And_OS_Fingerprinting_Lab/fping.txt`
 
IP subnet:10.142.111.240/24
This command sends ICMP requests to indentify hosts that are alive/up. 
The IPs that responded to the ping request:
10.142.111.1
10.142.111.6
10.142.111.48
10.142.111.96
10.142.111.99
10.142.111.100
10.142.111.240

- Run ping scan with nmap (any differences and why?)
Nmap identifies the PORTS and IPs open on the network, while fping only identifies the IPs open.
`nmap 10.142.111.240/24 -oN nmap.txt`
 
- Perform SYN scan against alive targets. Identify clients and servers.
`sudo nmap -sS 10.142.111.1,6,48,96,99,100,213`
Clients: 10.142.111.100 is a client because it did not respond to the syn scan and it did not listen for connections.
- Identify version of every daemon listening on the network
`sudo nmap -sV 10.142.111.1,6,48,96,99,100,213`
10.142.111.213 runs apache web server on non-standard port. (port 81) (this host also doesn't respond to pings.
- Identify, if possible, the OS running on each host
`sudo nmap -O 10.142.111.1,6,48,96,99,100,213`
#Tools
- fping
- nmap
