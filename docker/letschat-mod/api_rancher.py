import json
import requests
import os

def fetchcont(ranchersrv,service_name):
    project_url = 'http://'+ranchersrv+'/v1/projects/1a5/services'
    project_resp = requests.get(url=project_url)
    project_data = json.loads(project_resp.text)['data']
    for i in range(len(project_data)):
        if project_data[i]['name'] == service_name:
            service_id = project_data[i]['id']
            break
    url = 'http://'+ranchersrv+'/v1/projects/1a5/services/'+service_id+'/instances'
    service_resp = requests.get(url=url)
    service_data = json.loads(service_resp.text)['data']
    ret_txt = ""
    for i in range(len(service_data)):
        if i == len(service_data)-1:
            ret_txt = ret_txt+service_data[i]['primaryIpAddress']+":27017"
        else:
            ret_txt = ret_txt+service_data[i]['primaryIpAddress']+":27017,"
    print ret_txt

if __name__ == "__main__":
        rancher_server = os.environ['RANCHER_SERVER']
        service_name = os.environ['MONGO_SERVICE_NAME']
        fetchcont(rancher_server, service_name)
