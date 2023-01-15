import sys # sistema operativo
print(sys.path)

import re
text= "Mi número de telefono es 3124567845, el codigo del pais es 57 y mi número de la suerte es 3"

result = re.findall("[0-9]+", text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
final = time.asctime(local)
print(final)

import collections
number = [1,2,5,4,1,2,5,6,8,1]
counter = collections.Counter(number)
print(counter)