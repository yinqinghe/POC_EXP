import requests,threading,os,urllib3,time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from DrissionPage import ChromiumPage

#fofa: 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',

}
filename = Path(__file__).name.strip('.py')
line_break = '\n'
file_path=Path(__file__).resolve().parent
result_path=file_path/'result'/f'{filename}.txt'
page = ChromiumPage()

def poc(ip_, index):
    page.set.load_strategy.eager()
    page.new_tab(url=ip_)

    # page.get(ip_,timeout=8)
    if 'YApi' not in page.title:
        page.close_tabs()
        return
    print(page.title)
    ele = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div[4]/p[1]/a')
    # print(ele)
    print(ele.text.split(' ')[-1])
    page.close_tabs()
    return page

def exploit(ip_, index):
    try:
        page=poc(ip_, index)
        print('------',index%4)
        if index%4==0:
            print('+++++++',index%4)
            page.close_other_tabs(page.tab[0])
            page.close_other_tabs()
        # url = ip_+'downloader.php?file=%3Bpwd%00.zip'
        # # print(index,url)
        # res = requests.get(url, headers=headers, timeout=8, verify=False)
        # print(res, len(res.text))
        # print(index,ip_)
        # # with result_path.open('a+') as file:
        #     # file.write(ip_+line_break)

    except Exception as e:
        # print(e)
        pass

# url=''
# exploit(url,1)


threads = []
with open(r'D:\Downloads\tmp\yapi.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 55
        end = start+5

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            print(index, ip)
            # exploit(ip,index)

            thread = threading.Thread(target=exploit, args=(ip, index,))
            threads.append(thread)
pool_size = 20
# print(urls)

test = 'm'


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