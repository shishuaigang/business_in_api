import time
import rsa
import base64


class Login_Passwword_Encryption:
    def __init__(self, phonenumber, password):
        self.phonenum = phonenumber
        self.pwd = password

    def encryption(self):
        timesnap = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 获取时间戳，精确到秒
        with open('config/public.pem', 'rb') as f:
            pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())
        message = str(self.phonenum) + '#' + str(self.pwd) + '#' + timesnap
        encryption_text = rsa.encrypt(message.encode(), pubkey)
        return base64.encodebytes(encryption_text).decode().replace("\n", "")
