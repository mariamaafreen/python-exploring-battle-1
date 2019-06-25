
import socket   
 
hostname = socket.gethostname()    
ipaddr= socket.gethostbyname(hostname) 

print(" Computer Name is:" + hostname)    
print(" Computer IP Address is:" + ipaddr)       
    