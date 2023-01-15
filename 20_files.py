#abrir archivos use open
file = open("./text.text")
#Leer todo el texto .read()
#print(file.read())

#Leer linea a linea
#print(file.readline())

#permite leer linea y linea y no tomamos mucho espacio en memoria
for line in file:
  print(line)

#Libera la memoria de todo el texto
file.close()

#Se puede usar with para abrir el archivo realizar unas funciones y luego lo cierra automaticamente

with open("./text.text") as file:
  for line in file:
    print(line)


#open solo permiso de lectura
