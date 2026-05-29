valor = int(input("Digite um número inteiro positivo: "))

contador = 1
resultado = 0

while contador <= valor:
    resultado = resultado + contador
    contador += 1

print("A soma é:", resultado)