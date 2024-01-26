#coder and decoder using python
#condditions:
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

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