"""
numbers = []

for element in range(1,11):
  numbers.append(element *2)

print(numbers)

numbers_v2 = [element for element in range(1,11)]

print(numbers_v2)
"""

numbers = [i*2 for i in range(1,101) if i%2 ==0]

print(numbers)