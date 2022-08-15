food = ["pizza","hamburguer","hotdog","spaghetti","pudding"]

print(food[0]) #se precisamos acessar um elemento da lista nos colocamos a posição do vetor
print(food[0:3]) #podemos passar um inicio e fim para a lista

#a lista é algo mutavel e pode ser removidos ou inseridos caracteres na mesma.
food[0] = "banana"
print(food[0])

#Abrindo lista com for loops em coluna
for x in food:
    print(x, end=" ")

#Abrindo lista com for loops em linha
for x in food:
    print(x)

#algumas funções uteis para lista

food.append("ice cream") #adiciona elemento
print(food)
food.remove("ice cream") #remove elemento
print(food)
food.pop() #remove o ultimo elemento
print(food)
food.insert(0,"cake") #insere um elemento de acordo com o index
print(food)
food.sort() #ordena a lista
print(food)
food.clear() #limpa a lista
print(food)

# lista de listas chamadas de listas 2d (listas com multidimensões) ou object struct

food1 = ["pizza","hamburguer","hotdog","spaghetti","pudding"]
food2 = ["rice","bean"]
food3 = ["carrot","cucumber"]

storage_of_foods = [food1,food2,food3]
print(storage_of_foods)

#acessando a lista "pense no seguinte formato" -> uma caixa com os alimentos 1 e a primeira refeição selecionada
print(storage_of_foods[1][1])

