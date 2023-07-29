import sqlite3
import datetime

now = datetime.datetime.now()
now_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(now_time)

"""python连接sqlite数据库文件
"""
mydb = sqlite3.connect(r'D:\youxi\0x7eTools\Tools\WebShell\webshell_Manage\Godzilla\data.db')       # 链接数据库
cur = mydb.cursor()  


def sqlite(index,url):
                       # 创建游标cur来执行SQL语句
#  # 获取表名
#     cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
#     Tables = cur.fetchall()                     # Tables 为元组列表
#     print(Tables)
    # id="70c052ed-9c7d-4501-8751-5"+str(index)
    id="anfang"+str(index)
    payload_list=['JavaDynamicPayload','PhpDynamicPayload','AspDynamicPayload']
    Encryptor_list=['JAVA_AES_BASE64','JAVA_AES_RAW','PHP_XOR_BASE64','PHP_XOR_RAW']
    category="anfang"
    payload=payload_list[0]
    Encryptor=Encryptor_list[0]

    sqlite_sql_insert = """
    INSERT INTO "main"."shell" ("id", "url", "password", "secretKey", "payload", "cryption", "encoding", "headers", "reqLeft", "reqRight", "connTimeout", "readTimeout", "proxyType", "proxyHost", "proxyPort", "remark", "note", "createTime", "updateTime") VALUES ('"""+id+"""', '"""+url+"""', 'pass', 'key', '"""+payload+"""', '"""+Encryptor+"""', 'UTF-8', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
', '', '', 3000, 60000, 'NO_PROXY', '127.0.0.1', '8888', '备注', '', '"""+now_time+"""', '"""+now_time+"""');
    """
    sqlite_sql_select="SELECT id from shell where url='"+url+"'"
    
    
    res=cur.execute(sqlite_sql_insert)
    # print(res)
    res=cur.execute(sqlite_sql_select)
    # print(res.fetchall()[0][0])
    id=res.fetchall()[0][0]
    print(id)
    sqlite_sql_insert_one="""
    INSERT INTO "main"."shellEnv" ("shellId", "key", "value") VALUES ('"""+id+"""', 'ENV_GROUP_ID', '/"""+category+"""');
    """
    sqlite_sql_insert_two="""
    INSERT INTO "main"."shellEnv" ("shellId", "key", "value") VALUES ('"""+id+"""', 'ENV_ShellExecCommandPanel_Command_KEY', '');
    """
    res=cur.execute(sqlite_sql_insert_one)
    # res=cur.execute(sqlite_sql_insert_two)


with open(r'D:\BaiduNetdiskDownload\HACK\网络设备漏洞\海康威视\anfang_exp.txt', 'r') as file:
# with open(r'D:\BaiduNetdiskDownload\HACK\other\try\haikagn.txt', 'r') as file:
# with open(r'D:\BaiduNetdiskDownload\HACK\other\try\showDoc_godz.txt', 'r') as file:

    for index, line in enumerate(file):
            ip=line.strip('\n')
            
            print(index,ip)
            start=0
            end=start+250

            if index>=start and index<=end:
                sqlite(index,ip)
    


# sqlite()
cur.close()
mydb.commit()


