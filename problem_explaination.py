prefix sum
-----------
arr = [1, 2, 3, 4]
prefix = [0] * len(arr) --- [0,0,0,0] 

prefix[0] = arr[0] --- First prefix sum is always the first element itself. [1, 0, 0, 0]

for i in range(1, len(arr)): -- 1 Because we already handled index 0 here: prefix[0] = arr[0]

    prefix[i] = prefix[i-1] + arr[i]
   # prefix[i] -- sum of elements from index 0 to i
   # prefix[i-1] + arr[i] --- Previous total + current element

print(prefix)

Two Sum
-------

