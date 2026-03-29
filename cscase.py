import random
sneaks=['glock','ak47','awm','awp','gang','knife']
invent=[]
seil=[1000,2500,5000,10000]
coin=0

print('welcome')
v=True
while v==True:
    print('[0]Exit')
    print('[1]Case')
    print('[2]Invent')
    print('[3]Shop')
    print('[4]Balance')
    
    v1=int(input("print number"))
    if v1==0:
        print('Goodbuy')
        v=False
        break
    elif v1==1:
        item=random.choice(sneaks)
        c=random.choice(seil)
        print(f'Woooow:{item},{c}')
        invent.append(item)
        coin=coin+c
    elif v1==2:
        print(invent)
    elif v1==3:
        t=True
        while t==True:
            print('Welcome to magazine')
            print('[1] buy the glock, 1000$')
            print('[2] buy the ak47, 1500$')
            print('[3] buy the awm, 3000$')
            print('[4] buy the awp, 3000$')
            print('[5] buy the gang, 7000$')
            print('[6] buy the knife, 15000$')
            print('[0]Exit shop')
            v2=int(input())
            if v2==0:
                print(' ')
                v2=False
                break
            elif v2==1:
                coin=coin-1000
                if coin>=0:
                    print(' You buy glock')
                    invent.append(sneaks[0])
                else:
                    print("you don't have money")
                    coin=coin+1000
                    break
            elif v2==2:
                coin=coin-1500
                if coin>=0:
                    print(' You buy ak47')
                    invent.append(sneaks[1])
                else:
                    print("you don't have money")
                    coin=coin+1500
                    break
            elif v2==3:
                coin=coin-3000
                if coin>=0:
                    print(' You buy awm')
                    invent.append(sneaks[2])
                else:
                    print("you don't have money")
                    coin=coin+3000
                    break
            elif v2==4:
                coin=coin-3000
                if coin>=0:
                    print(' You buy awp')
                    invent.append(sneaks[3])
                else:
                    print("you don't have money")
                    coin=coin+3000
                    break
            elif v2==5:
                coin=coin-7000
                if coin>=0:
                    print(' You buy gang')
                    invent.append(sneaks[4])
                else:
                    print("you don't have money")
                    coin=coin+7000
                    break
            elif v2==6:
                coin=coin-10000
                if coin>=0:
                    print(' You buy knife')
                    invent.append(sneaks[5])
                else:
                    print("you don't have money")
                    coin=coin+10000
                    break
            
        
    elif v1==4:
        print(coin)
print('-----END-----')
