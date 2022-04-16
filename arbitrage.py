
##############################################################
print("What is your ASSet(eg:BTC):")                     #####
ASSet = input()                                          #####
print(f"your default price of {ASSet}:")                 #####
dEX=int(input())                                         #####
print(f"Your Exploit price of {ASSet}:")                 #####
eEX=int(input())                                         #####
print("Position size in decimal:")                       #####
pSIZE=float(input())                                       #####
print("Number of times trade will be executed:")         #####
nTIME=int(input())                                       #####
print("Potfolio:")                                       #####
pot = int(input())                                       #####
##############################################################


#find default share amount according to position size.
def DFSAAP(p,d):
    dfsaap = p*pot / d
    return dfsaap

#find exploit share amount according to position size.
def EFSAAP(p,e):
    efsaap = p*pot / e
    return efsaap

def difference(d,e):
    differ = d - e
    return differ

def change_to_cash(diff):
    ch = diff * eEX
    return ch

for i in range(nTIME):
    x=change_to_cash(difference(DFSAAP(pSIZE, dEX), EFSAAP(pSIZE, eEX)))
    print(f"Your {i} round profit is:")
    print(f"{int(x)}$")
    pot += x
print("Your New Portfolio is:")
print(f"{int(pot)}$")
