'''📝 Problem Statement:
A company maintains a daily shift schedule for its employees, where each employee is assigned a fixed position in an array
based on their order of work on Day 1.

To ensure fairness in work distribution, the company follows a policy where the schedule is adjusted every morning: the first
d employees are moved to the end of the schedule, preserving their order.

You are given the list of employee IDs for Day 1 and the value d. Write a program to compute the new schedule after applying
this policy.
Input:
schedule = [101, 102, 103, 104, 105]
d = 2

Output:
[103, 104, 105, 101, 102]

Explanation:
Employees 101 and 102 are shifted to the end of the schedule.'''

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n= len(arr)
        temp = [0]*n
        d =d%n
        for i in range(len(arr)):
            temp[(n-d+i)%n]=arr[i]
        for i in range(len(arr)):
            arr[i]=temp[i]
        return arr
arr=rotateArr()
arr=[101, 102, 103, 104, 105]
print(arr)


















        
