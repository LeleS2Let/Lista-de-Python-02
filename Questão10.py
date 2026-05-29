limite = float(input("Digite o orçamento disponível: "))

gasto_total = 0

while True:
    
    valor = float(input("Informe um gasto: "))
    
    if valor < 0:
        print("Programa encerrado.")
        break
    
    gasto_total += valor
    
    if gasto_total > limite:
        print("Orçamento ultrapassado!")
        break

restante = limite - gasto_total

print("Valor gasto:", gasto_total)
print("Saldo disponível:", restante)