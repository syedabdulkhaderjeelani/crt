a=[-20,-30,50,71]
b=[]
sum = 0
for i in range (0,len(a)):
    if(a[i]<0):
        b.append(a[i])
        sum = sum + b[i]
print(b)
print(sum)

