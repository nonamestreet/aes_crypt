import sys,rsa,struct,base64
from os.path import dirname, realpath, sep, pardir
#sys.path.append(dirname(realpath(__file__)))
from Crypto.Cipher import AES
from Crypto import Random
from argparse import ArgumentParser

#Author: Lin Sun
#https://github.com/nonamestreet/aes_crypt/

def encrypt(key_file):
    # Create a file object that produces random data when read from
    random = Random.new()
    # Generate a key if one was not supplied
    key = random.read(AES.key_size[0])
    key = base64.b64encode(key)
    encrypted_key=str(rsa.encrypt(key_file,key))
    sys.stdout.write(struct.pack("i"+str(len(encrypted_key))+"s",len(encrypted_key),encrypted_key))
    # Create the initialization vector
    iv = random.read(AES.block_size)
    sys.stdout.write(iv)
    # Create the cipher object and process the input stream
    cipher = AES.AESCipher(key, AES.MODE_CFB, iv)
    method = cipher.encrypt
    # Stream is processed below...
    # Process the input strea
    while True:
        data = sys.stdin.read(AES.block_size)
        if data == '': break # Check for EOF
        sys.stdout.write(cipher.encrypt(data))    
def decrypt(key_file):
    esize=struct.unpack_from("i",sys.stdin.read(4))[0]
    encrypted=struct.unpack_from(str(esize)+"s",sys.stdin.read(esize))[0]
    key=rsa.decrypt(key_file,encrypted)
    # Read in the initialization vector
    iv = sys.stdin.read(AES.block_size)
    # Create the cipher object and process the input stream
    cipher = AES.AESCipher(key, AES.MODE_CFB, iv)
    while True:
        data = sys.stdin.read(AES.block_size)
        if data == '': break # Check for EOF
        sys.stdout.write(cipher.decrypt(data))    
def main():
    parser = ArgumentParser(description=__doc__, epilog="""Input is read from
        stdin and output is written to stdout. Use the stream redirection
        features of your shell to pass data through this program. If a key is
        not specified, it is generated and written to stderr.""")
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-k', '--key_file', metavar='key_file',required=True,help="The public or private key file path. Public key for encryption and private key for decryption.")
    args = parser.parse_args()
    key_file=args.key_file
    if args.decrypt:
        decrypt(key_file)
    else:
        encrypt(key_file)

if __name__ == '__main__':
    main()
