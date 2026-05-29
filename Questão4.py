valor = int(input("Informe uma idade válida(0 a 150): "))

while valor >= 151 or valor < 0:
    print("Valor incorreto.")
    
    valor = int(input("Informe a idade novamente: "))

print("A idade informada foi:", valor)