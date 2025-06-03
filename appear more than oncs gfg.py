'''find the number that appear more than once
sample i/p = 1 2 3 4 4
output = 4'''

'''Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
Input: arr = [1, 2, 3, 3, 2, 1], x=2
Output: 2
Explanation: Frequency of 2 is 2.'''

class Solution:
    def findFrequency(self, arr, x):
        # code here
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=d.get(x)
        if(ans!=None):
            return ans
        elif ans==None:
            return 0
