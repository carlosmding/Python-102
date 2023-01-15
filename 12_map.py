numbers = [1,2,5,6,8,9,10]
numbers_2 =[2,3,8,9,10,11]
print(numbers)
numbers_v2  = [ x*2 for x in numbers]

#usando MAP se hace una transformacion a una lista
numbers_v3 = list(map(lambda i:i*2, numbers))
print(numbers_v3)

#hace la operacion con la longitud del menor
n4 = list(map(lambda x,y : x+y, numbers, numbers_2))
print(n4)


