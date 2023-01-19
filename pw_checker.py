# pw checker
username=input('username:')
pw=(input('password:'))
pw_length=len(pw)
security=('*' * pw_length)
print(f'your password {security} is {pw_length} long')
