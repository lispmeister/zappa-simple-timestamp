from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA
from base64 import b64encode

secret = "Change this to something unguessable!"
# Read secret key
f_key = open('./secret_key.pem').read()
key = DSA.import_key(f_key, passphrase=secret)

# Create message hash
message = b"2017-12-19T10:59:50.797961"
hash_obj = SHA256.new(message)
print('hash: ', b64encode(hash_obj.digest()))

# Sign the message hash
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)
print('signature: ', b64encode(signature))

# Load the public key
f = open("public_key.pem", "r")
pub_key = DSA.import_key(f.read())

# Create the hash again for verification
check_hash_obj = SHA256.new(message)
print('check_hash: ', b64encode(check_hash_obj.digest()))

# Verify the authenticity of the message
verifier = DSS.new(key, 'fips-186-3')
try:
    verifier.verify(check_hash_obj, signature)
    print("The message is authentic.")
except ValueError:
    print("Message failed authentication!")
