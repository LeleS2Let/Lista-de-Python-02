opcao = 1

while opcao != 3:
    
    print("\n1 - Adição")
    print("2 - Subtração")
    print("3 - Encerrar")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        valor1 = float(input("Informe o primeiro valor: "))
        valor2 = float(input("Informe o segundo valor: "))
        
        resultado = valor1 + valor2
        
        print("Total:", resultado)
    
    elif opcao == 2:
        valor1 = float(input("Informe o primeiro valor: "))
        valor2 = float(input("Informe o segundo valor: "))
        
        resultado = valor1 - valor2
        
        print("Resultado:", resultado)
    
    elif opcao == 3:
        print("Sistema finalizado.")
    
    else:
        print("Opção inválida.")