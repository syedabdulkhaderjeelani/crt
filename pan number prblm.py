"To check the pan number whether it is valid or not"

s=input()
digitcheck=s[5:9]
s1=s[0:5]


if(len(s)==10 and s[-1].isalpha() and digitcheck.isdigit() and s1.isalpha()):
    print('valid')
else:
    print('invalid')
    
    
