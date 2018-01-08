from flask import Flask
from flask import Response
import json
import datetime
from base64 import b64encode
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA


private_key_loc = './secret_key.pem'
secret = "Change this to something unguessable!"


def sign_data(data):
    '''
    param: string to be signed
    return: base64 encoded signature
    '''
    f_key = open(private_key_loc).read()
    key = DSA.import_key(f_key, passphrase=secret)
    hash_obj = SHA256.new(data.encode('utf-8'))
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return b64encode(signature)


app = Flask(__name__)


@app.route('/')


def index():
    timestamp = datetime.datetime.utcnow().isoformat()
    t_signature = sign_data(timestamp).decode('utf-8')
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
