

with open(r'D:\C#\VSCODE\python\POC_EXP\OA系统\泛微OA\result\fanwei_LoginSSO.txt','r') as f:
    file=f.readlines()


# print(file)

w=open(r'D:\C#\VSCODE\python\POC_EXP\OA系统\泛微OA\result\fanwei_LoginSSO_.txt','w')
for i in file:
    url=i.split('/upgrade')[0].split('://')[-1]
    print(url)
    w.write(url+'\n')
