import sqlite3
import datetime
import time
import socket

now = datetime.datetime.now()
now_time = now.strftime("%Y-%m-%d %H:%M:%S")
timestamp = str(time.time()*1000)

print(now_time)

"""python连接sqlite数据库文件
"""
mydb = sqlite3.connect(r'D:\youxi\0x7eTools\Tools\WebShell\webshell_Manage\Behinder\Behinder_v4.0.6\data.db')       # 链接数据库
cur = mydb.cursor()  


def sqlite(index,url):
    id=str(index)
    ip=url.split('//')[-1].split(':')[0]
    print(ip)
    # ip_address = socket.gethostbyname(domain_name)

    sqlite_sql_insert = """
    INSERT INTO "main"."shells" ("url", "password", "type", "catagory","addtime","updatetime","accesstime","ip","status","transProtocolId") VALUES ('"""+url+"""', 'Tas9er', 'jsp', '大华智慧园区', '"""+timestamp+"""', '"""+timestamp+"""', '"""+timestamp+"""', '"""+ip+"""', '0','-1');
    """
    sqlite_sql_select="SELECT id from shell where url='"+url+"'"
    
    
    res=cur.execute(sqlite_sql_insert)
    print(res)
    # res=cur.execute(sqlite_sql_select)
    # # print(res.fetchall()[0][0])
    # id=res.fetchall()[0][0]
    # print(id)
    # sqlite_sql_insert_one="""
    # INSERT INTO "main"."shellEnv" ("shellId", "key", "value") VALUES ('"""+id+"""', 'ENV_GROUP_ID', '/test');
    # """
    # sqlite_sql_insert_two="""
    # INSERT INTO "main"."shellEnv" ("shellId", "key", "value") VALUES ('"""+id+"""', 'ENV_ShellExecCommandPanel_Command_KEY', 'sh -c "{command}" 2>&1');
    # """
    # res=cur.execute(sqlite_sql_insert_one)
    # res=cur.execute(sqlite_sql_insert_two)


   
with open(r'D:\C#\VSCODE\python\POC_EXP\文件上传\大华智慧园区综合管理平台\result\大华智慧园区综合管理平台.txt', 'r') as file:
    for index, line in enumerate(file):
            ip=line.strip('\n')
            
            start=0
            end=start+10

            if index>=start and index<=end:
                print(index,ip)

                sqlite(index,ip)
    


# sqlite()
cur.close()
mydb.commit()


