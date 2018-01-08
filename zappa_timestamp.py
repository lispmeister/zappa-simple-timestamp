from flask import Flask
from flask import Response
import os
import json
import datetime
from base64 import b64encode
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA


def sign_data(data, key):
    '''
    param: string to be signed
    return: base64 encoded signature
    '''
    hash_obj = SHA256.new(data.encode('utf-8'))
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return b64encode(signature)


app = Flask(__name__)
secret = "Change this to something unguessable!"
secret_key = os.environ.get('secret_key')
key = DSA.import_key(secret_key, passphrase=secret)

@app.route('/')


def index():
    timestamp = datetime.datetime.utcnow().isoformat()
    t_signature = sign_data(timestamp, key).decode('utf-8')
    data = {
        'output': 'Signed timestamp',
        'timestamp': timestamp,
        'signature': t_signature
    }
    resp = Response(json.dumps(data))
    resp.headers['Content-Type'] = 'application/json'
    return resp


# We only need this for local development.
if __name__ == '__main__':
    app.run()
