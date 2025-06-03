'''Write a Python program that takes two integers n and m as input and computes a checksum using the following logic:
•	Count how many numbers from 1 to m are not divisible by n.
•	Count how many numbers from 1 to m are divisible by n.
•	Return the difference between these two counts:
not_divisible_count - divisible_count
________________________________________
Input Format:
•	First line: An integer n (the divisor)
•	Second line: An integer m (the upper bound)
________________________________________
Output Format:
•	A single integer representing the checksum
________________________________________
Example Input
n = 3
m = 10
Example Output:
4
Explanation:
Numbers from 1 to 10:
Divisible by 3 → 3, 6, 9 → count = 3
Not divisible by 3 → 1, 2, 4, 5, 7, 8, 10 → count = 7
Checksum = 7 - 3 = 4'''

n=int(input())
m=int(input())
count_div = 0
count_notdiv=0
for i in range (1,m+1):
    if i%n!=0:
        count_notdiv+=1
    
    else:
        count_div+=1
print(abs(count_notdiv-count_div))
        
    
    
    
























