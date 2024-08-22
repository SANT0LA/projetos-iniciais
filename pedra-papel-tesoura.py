import random
usuario= input("Escolha 1 para PEDRA, 2 para PAPAEL ou 3 para TESOURA ")
computador = random.choice(['1', '2', '3'])
#Levando em consideração que pedra ganha de tesoura, papel ganha de pedra e tesoura ganha de papel.
if usuario == computador:
    print("empate")
elif usuario == "1" and computador == "3" or usuario == "2" and computador == "1" or usuario == "3" and computador == "2":
    print("Você ganhou!!!")
else:
    print("perdeu!")
