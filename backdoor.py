import socketsserver
import OS
import platform

target = input('Enter the IP address to access: ')

print('Returning platform on target system' , platform.system())
print('Returning user logged in' , getlogin())
 

