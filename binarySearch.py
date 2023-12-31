import time
import random
def native_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1    

def binary_search(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1
    midpoint = (low+high)//2
    if l[midpoint]==target:
        return midpoint
    elif target <l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    else: #target > l[midpoint]:
        return binary_search(l,target,midpoint+1,high)

print(binary_search([1,2,3,4,5,6],6))

length = 1000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(0,4*length))
sorted_list = sorted(list(sorted_list))

start =time.time()
for target in sorted_list:
    native_search(sorted_list,target)
end=time.time()
print("Native search time = ", (end-start)/length,"Seconds ")

start =time.time()
for target in sorted_list:
    binary_search(sorted_list,target)
end=time.time()
print("Binary search time = ", (end-start)/length,"Seconds ")