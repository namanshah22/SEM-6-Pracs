import math
p,q = input('Enter two prime numbers: ').split()
plain = int(input('Enter the plain text: '))
p,q = int(p),int(q)
n = p*q
phi = (p-1)*(q-1)
def get_public_key(phi):
    e = 2
    while e < phi:
        if math.gcd(e,phi) == 1:
            break
        else:
            e += 1
    return e
e = get_public_key(phi)
def get_private_key(e,phi):
    d = 2
    while d < phi:
        if (d*e)%phi == 1:
            break
        else:
            d += 1
    return d
d = get_private_key(e,phi)
print('Public key(e,n): ',e,n)
print('Private key(d,n): ',d,n)
def enc(plain,e,n):
    return (plain**e)%n
cipher = enc(plain,e,n)
print('Cipher text: ',cipher)
def dec(cipher,d,n):
    return (cipher**d)%n
print('Plain text: ',dec(cipher,d,n))
