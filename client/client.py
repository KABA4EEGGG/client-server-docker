
#!/usr/bin/env python  
  
import http.client  
  

conn = http.client.HTTPConnection("localhost", 5555)

#request command to server  
conn.request("GET","/")  
#get response from server  
rsp = conn.getresponse()  
#print server response and data  
print(rsp.status, rsp.reason)  
data_received = rsp.read()  
print(data_received)  

conn.close()  
