import paramiko, re, time

host = '10.31.70.209'
user = 'restapi'
pswd = 'j0sg1280-7@'
port = 22


# stdin, stdout, stderr = client.exec_command('terminal lenght 0')
# stdin, stdout, stderr = client.exec_command('show interface')
#
# stdout.channel.recv_exit_status()
# lines = stdout.readlines()
# for line in lines:
#     print(line, end='')

def get_int():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=pswd, port=port)
    ssh = client.invoke_shell()
    ssh.send("\n\nterminal length 0\n\n")
    time.sleep(0)
    ssh.send("\nshow interfaces\n\n\n")
    time.sleep(1)
    ssh.close()
    return ssh.recv(5000).decode('utf-8').split('\n')

for i in get_int():
    if re.match(r'^[G|L]+', i): print((i.split()[0]))
    if re.match(r'\s+\d+?(?= packets input)', i): print(i.split()[0],' pkts in,', i.split()[3], ' bytes input')
    if re.match(r'\s+\d+?(?= packets output)', i): print(i.split()[0], ' pkts out,', i.split()[3], ' bytes out')

#print(get_int())