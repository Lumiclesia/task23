def changeAds(base10):
    # Write your code here
    base2=[]
    while True:
        if base10>=1:
            if (base10 % 2) ==1:
                base2.append("1")
            else:
                base2.append("0")
        else:
            break
        base10 = (base10 // 2)
        #print(str(base10))
    # print(base2)
    base2ok = []
    for digit in base2:
        base2ok.insert(0,digit)
        #print(f"{digit}, ,{base2ok}")
    # print(base2ok)
    return base2ok

def Negate(base2):
    negate2 = []
    for i in range(len(base2)):
        if base2[i]=='0':
            negate2.insert(i,'1')
        elif base2[i]=='1':
            negate2.insert(i,'0')
    return negate2

def Base2to10(base2):
    base10 = 0
    power = len(base2)
    indice = power-1
    for i in range(0, power):
        base10 += int(base2[i]) * pow(2,indice-i)
        # print(power, i, base2[i], base10, pow(2,power+1-i) )
    return base10

while True:
    n = input("Enter a number : ")
    try:
        if int(n) >=0:
            base2 = changeAds(int(n))
            negate2 = Negate(base2)
            base10 = Base2to10(negate2)
            print(f"Here is {n} convertion into Base 2 : {base2}")
            print(f"The negate binary of {base2} is : {negate2}")
            print(f"Here is {negate2} convertion into base 10 :{base10}")
            break
        else:
            print("Incorrect entry")
            continue
    except ValueError:
        print("Incorrect entry. You must enter a number !")
        continue




# Negate 
