#Tipos de errores
#error de sintaxis, revisar y corregirlo
#dividir por error
#print(0/0)

#NameError, variable no declara
#print(result)

suma = lambda x,y : x+y
assert suma(2,2) == 4
#permite validar la veracida de una función
#verificación prueba unitarias de cada método

print("Pasó correctamente")

#mis propios errores
#usa raise
age = 10
if age<18:
  raise Exception("No se permite menores de edad")
# Al lanzar un error se detiene el programa y continua las sgtes lineas de código
