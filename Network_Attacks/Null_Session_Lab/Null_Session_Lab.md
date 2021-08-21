#Null Sessions Lab - RCM 8/16/2021

#Description

In this lab you can practice different techniques and tools against a machine vulnerable to null session!

#Goal

The final goal of the lab is retrieve information from the target machine such as shares, users, groups and so on! Moreover by navigating the remote machine, you should be able to find a file name "Congratulations.txt\". Download it and explore its content.

#Tools

The best tools for this lab are:

    enum4linux

    samrdump

    smbclient

#Steps

1. Find a target in the network
`nmap -sn 192.168.99.100/24 -oN discoverynmap.txt`
Host `192.168.99.162` is up.

2. Check for null session
`nmap -sS -sV 192.168.99.162 -oN morenmap.txt`
   - Ports 135,139, and 445 are open.
   - Identified null session with `enum4linux -n 192.168.99.162`  
3. Exploit null session
   
    - Gather information with enum4linux
    - shares `nmap -script=smb-enum-shares 192.168.99.162`

       ```\\192.168.99.162\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
         ```

    - users `nmap -script=smb-enum-users 192.168.99.162`
     
        - Known Usernames: Administrator, eLS, Frank, Guest, HelpAssistant, netadmin

    - password policies 
      - no password expiries. some accounts disabled.
    - groups
      - WORKGROUP

5. Use smbclient to navigate the target machine
 
`sudo smbclient -L WORKGROUP -I 102.168.99.162 -N -U ""`
NONE OF THIS IS WORKING :) 
`smbclient \\\\192.168.99.162\\WorkSharing -N`
