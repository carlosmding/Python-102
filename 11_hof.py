def increment(x):
  return x +1

incrementv2 = lambda x:x+1

def hof (x, func):
  return x + func(x)

hofv2 =  lambda x, func : x + func(x)

result = hof(2, increment)
print(result)

resultv2 = hofv2(2, incrementv2)
print(resultv2)
#labmda puedo definirlas de forma dinámica sin usar una variable para almacenar su resultado

resultv3 = hofv2(2, lambda x:x+1)
print(resultv3)
