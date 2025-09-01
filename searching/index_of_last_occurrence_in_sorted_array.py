# 1. Naive Solution
l = [10,20,30,40,40,40,50,50]

def lastOcc(l, x):
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
    return -1

x = 50
print(lastOcc(l, x))


# 2. Solution: Through Binary Search
def lastOcc(l, x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid] < x:
            low = mid+1
        elif l[mid]>x:
            high = mid-1
        else:
            if mid==len(l)-1 or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid+1

    return -1
    
print(lastOcc(l, x))