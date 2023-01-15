set_countries = {"Col", "Mex", "Bol"}

size = len(set_countries)
print(size)
print("col" in set_countries)

set_countries.add("Per")
print(set_countries)

set_countries.update({"arg"})
print(set_countries)

#remove
set_countries.remove("arg")
print(set_countries)

#remover pero sin error si no está el elemento

set_countries.discard("arge")
set_countries.clear()
print(set_countries)

