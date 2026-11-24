# list, array, collection is same

# index =   0   1   2   3   4  5   6   7   8   9  
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]
# index = -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  

print(numbers[3], numbers[-3]) 

# list( start : end ) # start from the start index and stops before the end index
print(numbers[2:6]) # 2, 3, 4, 5
print(numbers[1:7])

# list(start : end : step)
print(numbers[1:7:1]) # skip 1 step  [56, 12, 89, 87, 32, 84]
print(numbers[1:7:2]) # [56, 89, 32]

print(numbers[7:2:-1]) # reversely skip 1 step  [59, 84, 32, 87, 89]
print(numbers[7:2:-2]) # [59, 32, 89]

print(numbers[4:]) # start 4 idx to last idx
print(numbers[:5]) # start 1st idx to 5 idx

print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) #shortcut to reverse a list