#coder and decoder using python
#check the terms and conditions in the readme.md file

x=input("enter  a input code:")
r=input("enter more than 7 random characters:")
i=0
if(len(x)>=3):
    for i in x:
        for j in r:
            print(r[:3]+x[1:]+x[0]+r[3:6])
            break
        break    
elif(len(x)<3):
    print(x[::-1])  
else:
    pass
y=input("enter a code to decode:")
c=0
if(len(y)<3):
    print(y[::-1])
elif(len(y)>=3):
    for c in y:
        print(y[-4]+y[3:-4])
        break
else:
    pass