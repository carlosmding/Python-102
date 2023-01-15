def increment(x):
  return x +1

rest2= lambda x : x + 1 #la misma funcion

res = increment(10)
print(res)
print(rest2(10))


full_name = lambda name, lastname: f"Full name is {name.title()} {lastname.title()}"

print(full_name("carlos", "pinto"))
