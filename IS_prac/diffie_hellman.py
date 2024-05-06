p = int(input("Enter p : "))
g = int(input("Enter g : "))
A = int(input("User 1 selects A as : "))
XA = (g**A) % p
print(f"User 1 sends XA i.e {XA} to User 2")
B = int(input("User 2 selects B as : "))
XB = (g**B) % p
print(f"User 2 sends XB i.e {XB} to User 1")
AK = (XB**A) % p
BK = (XA**B) % p
print(f"Both now have same secret key which is : ")
print(f"Ak : {AK}, Bk : {BK}")
