# aes_crypt
Encrypt stream of data using RSA key and AES in Python 2.7. You can encrypt arbitrary size data files/stream.

To Install:

_pycrypto_ is needed. Use pip to install:
```
pip install -r requirements.txt
```

To Use:

Encrypt sample_data with the public key _sample_public_
```
python aespipe.py -k sample_public < sample_data > sample_data_encrypted
```

Decrypt
```
python aespipe.py -d -k sample_private < sample_data_encrypted
```

