import hashlib
import math

p, q = input('Enter two prime numbers: ').split()
plain = input('Enter the plain text: ')
p, q = int(p), int(q)
n = p * q
phi = (p - 1) * (q - 1)

def get_public_key(phi):
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    return e

e = get_public_key(phi)

def get_private_key(e, phi):
    d = 2
    while d < phi:
        if (d * e) % phi == 1:
            break
        else:
            d += 1
    return d

d = get_private_key(e, phi)

print('Public key(e, n): ', e, n)
print('Private key(d, n): ', d, n)

def sign_message(message, private_key):
    hashed_message = hashlib.md5(message.encode()).digest()
    d, n = private_key
    md1 = int.from_bytes(hashed_message, byteorder='big')
    signature = pow(md1, d, n)
    print("Signature:", signature)
    print("md1:", md1)
    return signature, md1

def verify_signature(message, signature, public_key,md1):
    computed_hash = hashlib.md5(message.encode()).digest()
    e, n = public_key
    recovered_hash = pow(signature, e, n)
    md2 = int.from_bytes(computed_hash, byteorder='big')
    print("Recovered hash:", recovered_hash)
    print("md2:", md2)
    return md1 == md2

print("Message:", plain)

# Sign the message using the private key
signature, md1 = sign_message(plain, (d, n))

# Verify the signature using the public key
is_valid = verify_signature(plain, signature, (e, n),md1)
print("Signature is valid:", is_valid)
