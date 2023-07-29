import csv
from pathlib import Path

file_path = Path(__file__).resolve().parent

result_path = file_path/'result'/'yijian.csv'

with open(r'D:\C#\VSCODE\python\POC_EXP\文件上传\新开普智慧校园系统\result\新开普智慧校园系统.txt', 'r') as f:
    file_content = f.readlines()
print(file_content)
with result_path.open('w', encoding='utf-8') as file:
    for i in file_content:
        i = i.strip('\n')+'/mike.jsp'
        data = ["", "新开普智慧校园系统", "mike", 'jsp', i]

        writer = csv.writer(file)
        writer.writerow(data)
