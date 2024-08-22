import time

print("__________________________________")
print("Bem vindo ao contador de palavras!")
print("__________________________________")
time.sleep(3)
texto = input("Digite ou cole seu texto: ")
palavras = texto.split()
total_palavras = len(palavras)
print(total_palavras)