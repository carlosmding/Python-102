"""
dict = {}
for i in range(1,6):
  dict[i] = i*2

print(dict)

dict_v = {i:i*2 for i in range(1,6)}
print(dict_v)


name = ["nico", "juan", "pedro"]
age = [15, 56, 43]

person = list(zip(name, age))

new_dict = {name : age for (name, age) in person}
print(new_dict)

#opcion una sola linea
dict2 = {name : age for (name, age) in zip(name, age)}
print(dict2)



"""

import random
countries = ["col", "mex", "bol", "per" ]

population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

result={country:population for (country, population) in population_v2.items() if population > 20}
print(result)

text = "Hola, soy Carlos super poderosito"
unique = {c : c.upper() for c in text if c in "aeiou"}
print(unique)

total = {c : text.count(c) for c in text if c in "aeiou"}
print(total)

