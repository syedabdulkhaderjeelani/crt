n=int(input("number"))
sum = 0
count = 0
while(n>0):
    digit=n%10
    sum=sum + digit
    count=count + 1
    n=n//10
print("sum =",sum)
print("count=",count)
