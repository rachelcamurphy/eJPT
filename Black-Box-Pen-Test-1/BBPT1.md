#Rachel Murphy
#INE-8/20/21
#Black Box Pen Test 1

#Scenario
- You have been engaged in a Black-box Penetration Test (172.16.64.0/24 range). Your goal is to read the flag file on each machine. On some of them, you will be required to exploit a remote code execution vulnerability in order to read the flag.
- Some machines are exploitable instantly but some might require exploiting other ones first. Enumerate every compromised machine to identify valuable information, that will help you proceed further into the environment.
- If you are stuck on one of the machines, don't overthink and start pentesting another one.
- When you read the flag file, you can be sure that the machine was successfully compromised. But keep your eyes open - apart from the flag, other useful information may be present on the system.

#Goals
- Discover and exploit all the machines on the network
- Read all flag files (one per machine)

#What you will learn
- How to exploit Apache Tomcat
- How to exploit SQL server
- Post Exploitation Discovery
- Arbitrary file upload exploitation

#Recommended Tools
- Dirb
- Metasploit framework
- Nmap 
- Netcat

---

1. Find alive hosts on the network.

`nmap -sn 172.16.64.0/24`


