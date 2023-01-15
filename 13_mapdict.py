inventario = [
  {
    "product" : "camisa",
    "price": 100
  },
  {
    "product" : "pantalon",
    "price": 200
  },  
  {
    "product" : "tenis",
    "price": 500
  },
]

#transforma a un tipo diferente
prices =[product["price"] for product in inventario]
print(prices)

pricesv2 = list(map(lambda item: item["price"], inventario ))
print(pricesv2)

#agregar un nuevo atributo al diccionario -- pero eso no hace nada


"""
dictv =[item.update({"taxes" : item["price"]*.19}) for item in inventario]

#print(dictv)
#usando MAP

def add_taxes(item):
  item["taxes"] : item["price"] * 0.19
  return item
  
dictv2 = list(map(add_taxes, inventario ))
print("New Dic => ")
print(dictv2)
"""
#map no hace ajuste al array original idealmente 

def add_taxes(item):
  new_item = item.copy()
  new_item["taxes"] = new_item["price"] * 0.19
  return new_item
  
dictv2 = list(map(add_taxes, inventario ))

print("New Dic => ")
print(dictv2)

print("Old Dic => ")
print(inventario)



