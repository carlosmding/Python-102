# r solo permiso escritura
# w permiso de escritura
# r+ lectura y escritura al final
# \n => nueva linea
# w+ lectura y escritura pero sobreescribe el archivo

with open("./text.text", "w+") as file:
  for line in file:
    print(line)
  file.write("Nuevas cosas en este archivo \n") #crea directamente al final pero no como nueva linea a no ser que se use \n

with open("./text.text", "r") as file:
  for line in file:
    print(line)