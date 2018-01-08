from flask import Flask
from flask import Response
import json
import datetime
from base64 import b64encode
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA
import boto3


private_key_loc = 'secret_key.pem'
secret = "Change this to something unguessable!"
app = Flask(__name__)
BUCKET_NAME = 'zappa-4mp57o9mq'
KEY_NAME = private_key_loc
s3_resource = boto3.resource('s3')
secret_key_obj = s3_resource.Object(BUCKET_NAME, KEY_NAME)
secret_key_text = secret_key_obj.get()['Body'].read().decode('utf-8')
print(secret_key_text)
key = DSA.import_key(secret_key_text, passphrase=secret)



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
