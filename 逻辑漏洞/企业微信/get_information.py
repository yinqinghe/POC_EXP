import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
}

# url='http://106.52.27.241/cgi-bin/user/simplelist?access_token=boqqyDWq17jXjv9Nv4LaHwaaqBDAowqO1PwLMhCCp26kryNVKERMWcwjZhSuLQaLHtXiVyV2GRKiD437KLOMyU3JTyOOsjmArgH4JzXICzLYZgCIx7Br-zBJufGoRBgifcI55keTyRyzrNSENFnsXfw75Jfg4sAAAtAM90xu0iTpC28n4rpSY33rnpRXktwPdi7eBhN9w1Dioyp-rz800H8JP-j_RST_5g-gaexH5ls&department_id=DEPARTMENT_ID'


# url='https://106.52.27.241/cgi-bin/user/list_id?access_token=boqqyDWq17jXjv9Nv4LaHwaaqBDAowqO1PwLMhCCp26kryNVKERMWcwjZhSuLQaLHtXiVyV2GRKiD437KLOMyU3JTyOOsjmArgH4JzXICzLYZgCIx7Br-zBJufGoRBgifcI55keTyRyzrNSENFnsXfw75Jfg4sAAAtAM90xu0iTpC28n4rpSY33rnpRXktwPdi7eBhN9w1Dioyp-rz800H8JP-j_RST_5g-gaexH5ls'

url='https://106.52.27.241/cgi-bin/department/list?access_token=boqqyDWq17jXjv9Nv4LaHwaaqBDAowqO1PwLMhCCp26kryNVKERMWcwjZhSuLQaLHtXiVyV2GRKiD437KLOMyU3JTyOOsjmArgH4JzXICzLYZgCIx7Br-zBJufGoRBgifcI55keTyRyzrNSENFnsXfw75Jfg4sAAAtAM90xu0iTpC28n4rpSY33rnpRXktwPdi7eBhN9w1Dioyp-rz800H8JP-j_RST_5g-gaexH5ls&id='


payload={
	# "cursor": "xxxxxxx",
	"limit": 100
}

res=requests.post(url,data=payload,headers=headers, timeout=8, verify=False)

print(f'{res} {len(res.text)} \n {res.text}\n')


