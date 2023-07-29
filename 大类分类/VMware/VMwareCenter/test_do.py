import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'

# fofa:   title=" + ID_VC_Welcome + " && country="CN"

def exploit(ip_, index):
    try:

        url = ip_+''
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        # print(res, len(res.text))
        if 'ID_VC_Welcome' in res.text:
            print('可以正常访问')
        else:
            return
        get_url = ip_+'/ui/login'   #防止有些IP可以文件上传，修改admin密码，但不能网页无法登陆的情况
        get_res = requests.get(get_url, headers=headers, timeout=8, verify=False)
        if get_res.status_code==200:   
            print(index,ip_)
            print('可以登录')
            with result_path.open('a+') as file:
                file.write(ip_+line_break)
        else:
            return
    except Exception as e:
        # print(e)
        pass

# url='https://103.133.214.33'
# url='https://163.172.156.163'
url='https://27.125.42.206'
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\vmware.txt', 'r') as file:
    # with result_path.open('a+') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+10000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 20
# print(urls)

test = 'm'


if test=='t':
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
elif test=='m':
    # 创建线程池
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
        # 提交每个 URL 的请求任务
        futures = [executor.submit(exploit, url, index)
                   for index, url in enumerate(urls)]

        # 获取每个请求的结果
        for future in futures:
            result = future.result()