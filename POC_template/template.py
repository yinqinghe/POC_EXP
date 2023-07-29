with open(r'D:\C#\VSCODE\python\POC_EXP\010.py', 'r', encoding='utf8') as f:
    file = f.readlines()

print(file)


with open(r'D:\C#\VSCODE\python\POC_EXP\test.py', 'a+', encoding='utf8') as f:

    for i in file:
        print(i)
        i = i.strip('\n')
        print(i)
        ii = f'"{i}",\n'
        # print(ii)
        f.write(ii)
