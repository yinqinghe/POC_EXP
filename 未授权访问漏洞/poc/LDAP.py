import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
from pathlib import Path
import subprocess
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import ldap3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path = Path(__file__).resolve().parent
result_path = file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    # 设置LDAP服务器连接信息
    addr=ip_.strip('\n')
    server = ldap3.Server(f'ldap://{addr}',connect_timeout=8)
    base_dn = ''

    # 尝试连接LDAP服务器
    try:
        conn = ldap3.Connection(server, auto_bind=True)
        
        res=conn.search(base_dn, '(objectclass=*)')
        ip=addr.split(':')[0]
        
        print(index,ip)
        print(res)
        print('LDAP connection successful.')
        # with result_path.open('a+') as file:
            # file.write(ip+line_break)
    except ldap3.core.exceptions.LDAPException as e:
        # print('LDAP connection failed:', e)
        pass

# url=''
# exploit(url,1)

# 113.108.97.122
# 14.136.19.106

threads = []
with open(r'D:\Downloads\tmp\Ldap.txt', 'r') as file:
    # with result_path.open('a+') as file:
    urls = []
    for index, line in enumerate(file):
        start = 300
        end = start+100

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 30
# print(urls)

test = 'm'


if test == 't':
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
elif test == 'm':
    # 创建线程池
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        # 提交每个 URL 的请求任务
        futures = [executor.submit(exploit, url, index)
                   for index, url in enumerate(urls)]

        # 获取每个请求的结果
        for future in futures:
            result = future.result()
