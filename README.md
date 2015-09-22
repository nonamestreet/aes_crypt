# aes_crypt
Encrypt stream of data using RSA key and AES in Python 2.7. You can encrypt arbitrary size data files/stream. You can use it to encrypt huge files. You can find more information here: http://stackoverflow.com/questions/7143514/how-to-encrypt-a-large-file-in-openssl-using-public-key

To Install:

_Python2.7_ and _pycrypto_ is needed. Use pip to install:
```
pip install -r requirements.txt
```

To Use:

Encrypt sample_data with the public key _sample_public_
```
python aespipe.py -k sample_public < sample_data > sample_data_encrypted
```

Decrypt:
```
python aespipe.py -d -k sample_private < sample_data_encrypted
```

A little help:
```
python aespipe.py --help
```

You can generate the key pair using:
```
openssl genrsa -out mykey.pem 1024
openssl rsa -in mykey.pem -pubout > mykey.pub
```