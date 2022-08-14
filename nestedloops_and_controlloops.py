# from symtable import Symbol


# rows = int(input("quantas linhas?: "))
# columns = int(input("quantas colunas?: "))
# symbol = input("enter um simbolo para usar: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

#------------------------------------------------CONTROL CONDITIONS ---------------------------------------#
#breaks: objetivo interromper o loop enquanto ele for True.
#continue pula para a proxima iteração do loop
#pass nao faz nada atua como placeholder
#Ex:

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break 
    
phone_number = "123-456-7890"
spacename = "Vinicius-Dias-Barros"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")
    
# for i in spacename:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

