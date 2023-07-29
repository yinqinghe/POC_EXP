import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
from concurrent.futures import ThreadPoolExecutor

headers={
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
}

# print(file)
#users.data
def exploit(ip_,index):
    try:
        
        command =f"mount -t nfs {ip_}:/ /mnt"
        res=os.popen(command).read()
        if 'denied' in res or 'not supported' in res:
            return
        print(len(res))
        print(index,res)
        # print(get_res.text)
        with open(r"result.txt", "a+") as file:
                file.write(ip_+"\n")
         
    except Exception as e:
        pass

# url="https://sso.elms.edu:9443"
# exploit(url)



threads=[]
# with open(r'D:\Downloads\tmp\nfs.txt', 'r') as file:
with open(r'nfs.txt', 'r') as file:
    urls=[]
    for index, line in enumerate(file):
        urls.append(line.strip('\n'))
        # start=0+int(sys.argv[1])*20
        start=0
        end=start+2000

        if index>=start and index<=end:
            # if index==:
                # break
            ip=line.strip('\n')
            print(index,ip)
            exploit(ip)



pool_size = 30
# print(urls)
# 创建线程池
with ThreadPoolExecutor(max_workers=pool_size) as executor:
    # 提交每个 URL 的请求任务
    futures = [executor.submit(exploit, url,index) for index, url in enumerate(urls)]

    # 获取每个请求的结果
    for future in futures:
        result = future.result()