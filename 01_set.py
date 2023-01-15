set_countries = {"Col", "Mex", "Bol"}
print(set_countries, type(set_countries))
# si hay elementos repetidos, estos no se imprime o se usan

set_types = {1, "hola", False, 12.12}
print(set_types)

#creando un conjunto con metodo SET
set_from_string = set("hola")
print(set_from_string)

new_list = list(set_from_string)
new_list.sort()
print(new_list)

# crear a partir de una tupla
set_from_tuple = set(("abc", "def"))
print(set_from_tuple)
