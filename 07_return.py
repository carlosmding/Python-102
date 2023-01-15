"""
def suma_range (a, b):
  sum = 0
  for x in range(a,b+1):
    sum += x
  return sum

print(suma_range(1,10))

"""

def find_volume(lenght=1, width=1, depth=1):
  return lenght*width*depth, "hola", depth*2

result = find_volume(5,6,8)
print(result)


#valores por defecto en caso que no los envien y evitar el error

res_sinparametros = find_volume()
print(res_sinparametros)

#tambien puedo enviarle solo un parametro si asi deseo

print(find_volume(width = 5) )

#se pueden retornar varias variables y devuelve eso en una tupla a una sola variable 

