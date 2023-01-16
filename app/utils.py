def get_population():
  keys = ["Col", "Bol"]
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item : item["Country"] == country, data))
  return result

def find_country(find_country, data):
  for pais in data:
    if pais["Country/Territory"] == str(find_country):
      return pais

def create_values(pais):
  labels =[]
  values =[]
  for data in pais:
    if "Population" in data:
      labels.append(data)
      values.append(pais[data])
  return labels, values


  