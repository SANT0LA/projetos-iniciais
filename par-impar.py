#O famoso sistema para ver se um número é par ou impar. XD
numero = int(input("Digite um número: "))
resto = numero % 2
if resto == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar!")