set_a = {"Col", "Mex", "Bol"}

set_b = {"Per", "Bol"}

set_c = set_a.union(set_b)
print(set_c)
#tambien se puede hacer con el operador barrita

set_d = set_a.intersection(set_b)
print(set_d)

#tambien con operador ampersan & 

#diferencia restarle a A lo que hay en B

set_c = set_a.difference(set_b)
print(set_c) # tambien con resta

# diferencia simética, hacer unión y quitar los elementos en común 

#diferencia simétrica

set_e = set_a.symmetric_difference(set_b)
print(set_e) # ambien usar signo gorrito
