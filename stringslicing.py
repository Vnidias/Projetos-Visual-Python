#slicing = creating a substring from a element
# comumente construido no seguinte formado indexing[] or slice()
                # regra [start:stop:step]
                
name = input("Digite seu nome completo utilizando espacos e sem caracteres especiais: ")

firstname = name[0:8:1]
print("meu firstname é:" + firstname)
nome, sobrenome, ultimonome = name.split(" ")

print(nome)
print(sobrenome)
print(ultimonome)
