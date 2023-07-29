

# from pathlib import Path
# string = "systeminfo"

# exist = ['whoami', 'ipconfig', 'systeminfo']

# # if string in exist:
# #     print('yes')

# # 获取当前文件的文件名
# filename = Path(__file__).name.strip('.py')

# # 打印文件名
# print(filename)

import time

timestamp = int(time.time()*1000)
print(timestamp)

import socket

# domain_name = 'fymanage.fyskjg.com'
domain_name='14.21.88.94'
ip_address = socket.gethostbyname(domain_name)
print(ip_address)