import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

#Author: Lin Sun
#https://github.com/nonamestreet/aes_crypt/
def encrypt(key_file,msg):
    fh=open(key_file,"r")
    publickey=RSA.importKey(fh.read())
    fh.close()
    encrypted = publickey.encrypt(msg, 32)
    return encrypted

def decrypt(key_file,encrypted):
    fh=open(key_file,"r")
    privatekey=RSA.importKey(fh.read())
    fh.close()
    decrypted = privatekey.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted


