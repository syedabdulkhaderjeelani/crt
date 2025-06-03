def print_nat(n):
    fact=n
    if (n==0):
        return 1
    else:
         fact=fact*print_nat(n-1)
         return fact
ans= print_nat(5)
print(ans)
