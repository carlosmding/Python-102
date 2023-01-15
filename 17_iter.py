for i in range(1,11):
  print(i)

#podemos controlar como se ejecuta un iterable iter()
my_iter = iter(range(1,11))
print(my_iter)

#iter de forma manual con funcio next()
#crea el array progresivamente no lo crea inmediatamente, entonce no hay problema con uso excesivo de memoria
print(next(my_iter))

# si iterando manueal me paso del limite superior saca el error StopIteration
