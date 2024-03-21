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

n = input("Enter a number : ")
base2 = changeAds(int(n))
negate2 = Negate(base2)
print(f"Here is {n} convertion int Base 2: {base2}")
print(f"The negate binary of {base2} is : {negate2}")


# Negate 
