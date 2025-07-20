# p1
##--- From 'a3b2c1' → Output: 'aaabbc'
s = 'a3b2c1'
output = '' --- no space

for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i+1])
    output += char * count

print(output)
### o/p: aaabbc

# Each step explaination 
# for i in range(0, len(s), 2): --- why 2
# A: i = 0, 2, 4 ... 0 = a,2 = b, 4 = 1 ---  to pick only the characters (letters)
# char = s[i] (get letter)
# count = int(s[i+1]) (get number right after letter) -- next number
# multiply number with letter in n times(number)

# P2
##--- 

