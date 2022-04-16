from data import data,decode

def entry():
    print("what service do you want:")
    print("1.Encrypt")
    print("2.Decrypt")
    e = int(input(': '))
    return e

inputt = ""
ent = entry()
if ent > 2:
    print("choose between 1 and 2")
    entry()
if ent == 1:
    print("Please Input Data:")
    inputt = input()
    cdata = data(inputt)
    key_1, key_2 = cdata.encrypt_data() 
    print("Your encrypted data is:")
    print(key_2)
    print("Your Dummy key is:(don't lose or reveal)")
    print(key_1)
if ent == 2:
    print("Encrypted Data:")
    encd = input()
    print()
    print("Dummy key:")
    dum = input()
    decoder = decode(int(dum),int(encd))
    print()
    print("Your Decoded Data is:")
    print(decoder.decode_data())
    


