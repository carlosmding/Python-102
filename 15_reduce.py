import functools

numbers = [1,2,3,4]
result = functools.reduce(lambda counter, number : counter + number, numbers )

print(result)