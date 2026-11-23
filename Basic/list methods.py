numbers = [12, 45, 98, 68]

numbers.append(56) # add 56 at last
print(numbers)

numbers.insert(0, 71) # (idx, value)
numbers.insert(2, 81)
print(numbers)

if 98 in numbers: 
    numbers.remove(98) # 98 remove
if 8 in numbers:
    numbers.remove(8)
print(numbers)

last = numbers.pop() # remove last element
print(last, numbers)

if 5 in numbers:
    index = numbers.index(5) # serach 
    print(index)

numbers.sort() # sort 
print(numbers)

numbers.reverse() # reverse
print(numbers)