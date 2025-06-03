'''input =  1 2 2 2 4 3 3 1
find max and min freq'''

arr=[1,2,2,2,4,3,3]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
print(freq)
maxi = max(freq,key=freq.get)
mini = min(freq,key=freq.get)
print(maxi)
print(mini)
