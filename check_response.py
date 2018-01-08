from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA
from base64 import b64decode
import json


# Load the public key
f = open('public_key.pem', 'r')
pub_key = DSA.import_key(f.read())

# Read JSON input
json_string = '{"output": "Signed timestamp", "timestamp": "2017-12-19T14:07:39.149933", "signature": "qJVvJcBTUxpv63chyx3dCt43YueMe4fF8/G/qsRHbriSflkHIfUIgSM6rCy387Hx811zxHXSs34="}'
parsed_json = json.loads(json_string)
timestamp = parsed_json['timestamp']
print('timestamp: ', timestamp)
signature = parsed_json['signature']
print('signature: ', signature)

# Create the hash for verification
hash_obj = SHA256.new(timestamp.encode('utf-8'))
print('hash: ', hash_obj.digest())

# Verify the authenticity of the message
verifier = DSS.new(pub_key, 'fips-186-3')
try:
    verifier.verify(hash_obj, b64decode(signature))
    print('The message is authentic.')
except ValueError:
    print('Message failed authentication!')
