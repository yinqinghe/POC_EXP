from DrissionPage import ChromiumPage
from pathlib import Path


line_break = '\n'

filename = Path(__file__).name.strip('.py')
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'


page = ChromiumPage()
# page.get('https://www.baidu.com')
def open_tab(url,index):
    page.new_tab(url)
    username = page.ele('xpath://*[@id="app"]/main/div[2]/div/form/div[1]/div/div/span/span/input')
    if not username:
        page.ele('xpath://*[@id="details-button"]').click()   #点击高级按钮
        page.ele('xpath://*[@id="proceed-link"]').click()     #确认URL跳转

    username.input('admin')
    password=page.ele('xpath://*[@id="app"]/main/div[2]/div/form/div[2]/div/div/span/span/input')
    password.input('admin')
    submit=page.ele('xpath://*[@id="app"]/main/div[2]/div/form/div[3]/div/div/span/button')
    submit.click()

with open(r'D:\C#\VSCODE\python\POC_EXP\批量工具\白嫖V2ray\result\ex.txt', 'r') as file:

    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+4

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            ip = line.strip(line_break)
            print(index, ip)
            open_tab(ip,index)