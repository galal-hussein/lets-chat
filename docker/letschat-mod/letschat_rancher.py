import os
import socket
import dns.resolver

def fetchcont(service_name):
    arecords = dns.resolver.query(service_name,'A')
    ret_txt = ""
    for i in range(len(arecords)):
        if i == len(arecords)-1:
            ret_txt = ret_txt+str(arecords[i])+":27017"
        else:
            ret_txt = ret_txt+str(arecords[i])+":27017,"
    print ret_txt

if __name__ == "__main__":
        service_name = os.environ['MONGO_SERVICE_NAME']
        fetchcont(service_name)
