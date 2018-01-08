from Cryptodome.PublicKey import DSA

# Create a new DSA key
secret_code = "Change this to something unguessable!"
key = DSA.generate(2048)
encrypted_key = key.exportKey(passphrase=secret_code, pkcs8=True,
                              protection="PBKDF2WithHMAC-SHA1AndDES-EDE3-CBC")
public_key = key.publickey().exportKey(format='PEM')
f_sec = open("secret_key.pem", "wb")
f_sec.write(encrypted_key)
f_pub = open("public_key.pem", "wb")
f_pub.write(public_key)
