
# f = open(r'D:\C#\VSCODE\未授权访问漏洞\poc\extra_tools\ldap.txt', 'w')


with open(r'D:\Downloads\tmp\vnc.txt', 'r') as file:
    urls = []
    content=''
    for index, line in enumerate(file):
        start = 1000
        end = start+20

        if index >= start and index <= end:
            content=content+line.split(':')[0]+'-'
            print(line.split(':')[0])
        # f.write(line.split(':')[0]+'\n')
print(content)
# f.close()

# import ldap3

# # 设置LDAP服务器连接信息
# # server = ldap3.Server('ldap://contacts.pratt.edu:389',connect_timeout=8,get_info=all)
# server = ldap3.Server('ldap://61.155.146.162:389',connect_timeout=8,get_info=all)

# base_dn = ''

# # 尝试连接LDAP服务器
# try:
#     conn = ldap3.Connection(server, auto_bind=True)
#     conn.search(base_dn, '(objectclass=*)')
#     print('LDAP connection successful.')
# except ldap3.core.exceptions.LDAPException as e:
#     print('LDAP connection failed:', e)
# # finally:
#     # conn.unbind()

