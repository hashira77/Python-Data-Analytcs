while True:
username = input("Enter a usrname: ")
password = input("Enter a password: ")
if username == 'admin' and password == 'password':
    print('Login Successful')
    break
else:
    print('Login failed')