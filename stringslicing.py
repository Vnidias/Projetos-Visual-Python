#slicing = creating a substring from a element
# comumente construido no seguinte formado indexing[] or slice()
                # regra [start:stop:step]
                # caso voce nao preencha o start e o stop ele assumira no start o começo da string e no stop
                # o final da string
                
#name = input("Digite seu nome completo utilizando espacos e sem caracteres especiais: ")

name = "Vinicius Dias Barros"
firstname = name[0:8:1]
lastname = name[8:13:1]
print("meu firstname é:" + firstname)
print("meu sobrenome é:" + lastname)

nome, sobrenome, ultimonome = name.split(" ")

print(nome)
print(sobrenome)
print(ultimonome)

reversed_name = name[::-1]
print(reversed_name)