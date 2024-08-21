#O objetivo desse codigo será fazer um gerador de senhas aleatorias de acordo com o número de caracteres
#especificados e se possivel vincular essas senhas geradas a um banco de dados. :)
import random
import string
print("============================================================================================================")
print("AVISO!!! ESSE GERADOR DE SENHA NÃO SEGUE(AINDA) OS PADRÕES DE SEGURANÇA ADEQUADOS. FINS APENAS EDUCACIONAIS.")
print("============================================================================================================")
tamanho_senha = int(input("Digite o número de caracteres da senha: "))
caracteres = string.ascii_letters
caracteres += string.digits
caracteres += string.punctuation

senha = ""

for i in range(tamanho_senha):
    proximo_caracter = random.choice(caracteres)
    senha += proximo_caracter
print("sua senha aleatoria é: ", senha)