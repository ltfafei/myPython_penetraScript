
import requests, base64

url = 'http://192.168.212.106/'
username = b'admin'
passwd = b'admin'

user_pass_encode = base64.b64decode('{0}:{1}'.format(username, passwd))
print(user_pass_encode)