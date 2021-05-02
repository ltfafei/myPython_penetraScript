user = raw_input('username:')
passwd = raw_input('password:')

name = 'admin'
pw = 'admin888'

if name == user:
    if pw == passwd:
        print('login successful')

    else:
        print('password false')
else:
    print('username false')