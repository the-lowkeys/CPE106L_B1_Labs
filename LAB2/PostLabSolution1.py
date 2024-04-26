"""
stats.py
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
    freq = max(list(map(lst.count, lst))) #finds what number shows up more often
    mode = list(set(filter(
        lambda x: lst.count(x) == freq, lst))) #func to see other modes; numbers with equal freq
    return mode # returns a list

mode = compMode(userlist)
print("The mode is" , mode)


def compMean(lst):
    mean = sum(lst) / len(lst)
    return mean

mean = compMean(userlist)
print("The mean is" , mean)


