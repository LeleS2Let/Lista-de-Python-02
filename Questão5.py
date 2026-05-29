total = 0

valor = int(input("Informe um número inteiro: "))

while valor != 0:
    total = total + valor
    
    valor = int(input("Digite outro valor (0 para finalizar): "))

print("Resultado da soma:", total)