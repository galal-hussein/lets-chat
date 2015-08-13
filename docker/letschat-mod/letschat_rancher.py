import os
import socket
import DNS

def fetchcont(service_name):
    query = DNS.dnslookup(service_name,'A') 
    ret_txt = ":27017,".join(query)+":27017"
    print ret_txt

if __name__ == "__main__":
        service_name = os.environ['MONGO_SERVICE_NAME']
        fetchcont(service_name)
