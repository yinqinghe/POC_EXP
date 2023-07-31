import paramiko

host = '44.196.3.129' 
port = 22  
username = 'zero'  
password = 'Root@428'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=port, username=username, password=password)

stdin, stdout, stderr = client.exec_command('whoami')

for line in stdout:
    print(line.strip('\n'))

client.close()