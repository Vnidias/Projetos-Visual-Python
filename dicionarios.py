#Dicionarios sao mutaveis, uma coleção nao ordenada de pares chave:valor são rapidos porque usao hashing o que nos permite acessar um valor rapidamente.

contatos = {'Yan': '1234-5678'}
print(type(contatos))

contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]

contatos = dict(contatos_lista)
print(contatos)

#-------------------------------------------------------------------------------------------------------------

capital = {'USA':'Washington DC', 
           "India": "New Dehli",
           "China": "Beijing",
           "Russia": "Moscow"}

# #analisando um caso especifico
# print(capital['Russia'])

# #buscando um valor no dicionario
# print(capital.get("Germany"))

#buscando uma chave no dicionario
# print(capital.keys())

# #buscando um valor no dicionario
# print(capital.values())

# #buscando todos os items no dicionario
# print(capital.items())

# #--------------------------------------------------------

# #Acessando dicionario no for loop

# for key,value in capital.items():
#     print(key,value)

# #Alterando o dicionario e inserindo um valor

# capital.update({"Germany":"Berlin"})
# print(capital)

# #Alterando um elemento ja existente e inserindo um valor

# capital.update({"USA":"BLABLABLA"})
# print(capital)

#Eliminando um elemento

capital.pop("USA")
print(capital)

#Limpando um dicionario

capital.clear()
print(capital)