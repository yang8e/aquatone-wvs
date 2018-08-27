import os
import re
import paramiko
import smtplib

def sendmail(message):
	smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('2222@live.cn','1111')
	smtpObj.sendmail('2222@live.cn','33333@qq.com',message)
	smtpObj.quit()


print('input urls------------------:')

input_url = input()
#远程连接服务器，进行信息收集，并下载到本地
transport = paramiko.Transport(('1.1.1.1', 22))
transport.connect(username='root', password='1111111')
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin,stdout,stderr = ssh.exec_command('python /root/server.py '+input_url)
cat_ = stdout.read().decode()
print(cat_)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/root/aquatone/'+input_url+'/urls.txt', 'urls.txt')
#---------------------------------------------------

ls=open('urls.txt')
for i in ls: 
	get_ip = i.strip('\n')
	try:
		out_bytes = subprocess.run(['wvs_console.exe','/scan',get_ip],timeout=7200)
		out_text = out_bytes.decode('utf-8')
		print(out_text)
	except subprocess.TimeoutExpired:
		print('timeout,error')
	if '0 high' in out_text or 'No alerts found' in out_text:
		print('don\'t need look '+i+'\n\n')
	else:
		sendmail(out_text)
