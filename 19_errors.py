#Manejo y control de errores
#try

try:
  print(0/0)
except ZeroDivisionError as error:
  print(error)
  
try:
  assert 1 != 1, "Uno no es igual a uno"
except AssertionError as error:
  print(error)

try:  
  age = 10
  if age<18:
    raise Exception("No se permite menores de edad")
except Exception as error:
  print(error)


print("Hola")

#Se pueden reunir un solo bloque de try el bloque de codigo y luego todas las except seguidas