#set é uma coleção nao ordenada e nao indexada que NAO PERMITE VALORES DUPLICADOS

utensilios = {"fork","spoon","knife"}
dishes = {"bowl","plate", "cup","knife"}

new = {"fork","spoon","knife"}
new2 = {"bowl","plate", "cup","knife"}

# for i in utensilios: #mais rapido que uma lista
#     print(i)
    
# utensilios.add("napkin")
# utensilios.remove("napkin")
# utensilios.clear() # limpa tudo

#atualizando o set com o metodo update "Ele pega todos os elementos passados e atualiza o set de referencia"

# utensilios.update(dishes)
# print(utensilios)

#union um pouco similar ao update, mas o update pode fazer a atualização de um elemento enquanto o union carrega todos os objetos.
# utensilios.union(dishes)
# print(utensilios)

#verificando itens diferentes entre listas

print(new.difference(new2)) # compara os itens da primeira lista com a segunda como temos faca entre as duas os dois que restam diferentes sao printados
print(new.intersection(new2))