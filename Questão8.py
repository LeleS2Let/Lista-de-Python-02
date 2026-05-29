primeiro = int(input("Digite o número inicial: "))
ultimo = int(input("Digite o número final: "))

numero = primeiro

while numero <= ultimo:
    
    if numero % 2 == 0:
        print(numero)
    
    numero += 1