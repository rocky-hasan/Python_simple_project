from cryptography.fernet import Fernet


def write_key():
    key=Fernet.generate_key()
    with open('key.key', 'rb') as file_key:
        file_key.write(key)
write_key()
def load_key():
    file=open('key.key','rb')
    key=file.read()
    file.close()
    return key


out_password=input("Enter your password:")
key=load_key() + out_password.encode()
fer=Fernet(key)


def view():
    with open('template.txt','r') as r:
        for line in r.readlines():
            data = line.rstrip()
            user,password=data.split("|")
            print(f'Username: {user} Password: {str(fer.decrypt(password.encode()))}')
        
def add():
    username=input("Enter username:")
    password=input("Enter password:")
    with open('template.txt','a') as f:
        f.write(username + '|' + str(fer.encrypt(password.encode()).decode()) +'\n')


while True:
    mode=input("add a new password or view existing ones(view,add) or quit press to exit: ").lower().strip()
    if mode=='quit':
        break
    elif mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print("invalid Data")
        continue