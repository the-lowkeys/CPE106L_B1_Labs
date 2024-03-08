"""
Statisticians would like to have a set of functions
to compute the median and mode of a list of numbers.
The median is the number that would appear at the
midpoint of a list if it were sorted. The mode is
the number that appears most frequently in the list.
Define these functions in a module named stats.py.
Also include a function named mean, which computes
the average of a set of numbers. Each function expects
a list of numbers as an argument and returns a single number.
"""

print("Input numbers, and type '-999' if done")

num = 0
userlist = []

while num != (-999):
    num = int(input("Enter value: "))
    userlist.append(num)

userlist.remove(-999)

print("List:" , userlist) 
print("List Length:" , len(userlist))

def compMedian(lst):
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        x = length//2
        median = (lst[x-1]+lst[x])/2
    else:
        x = (length-1)//2
        median = lst[x]
    return median

median = compMedian(userlist)
print("The median is" , median)


def compMode(lst):
    
    return mode


def compMean(lst):
    mean = sum(lst) / len(lst)
    return mean

mean = compMean(userlist)
print("The mean is" , mean)
