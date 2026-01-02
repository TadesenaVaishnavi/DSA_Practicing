# https://chatgpt.com/share/69576150-ac30-8007-a439-86c80d5cc29c --- chatgpt link
# binarysearch

def binarysearch(list1, key):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high) // 2

        if key == list1[mid]:
            return True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False
list1 = [2,5,3,4,1,3]
list1.sort()
key = 1
binarysearch(list1, key)


 # linearsearch

def linearsearch(list1, key):
    for i in range(len(list1)):
        if list1[i] == key:
            return True
    return False
list1 = [2,5,3,4,1,3]
key = 1
linearsearch(list1, key)
