quantidade_horas = int(input("Informe quantas horas serão analisadas: "))

controle = 1
total_produzido = 0

while controle <= quantidade_horas:
    pecas = int(input("Quantidade produzida na hora: "))
    
    total_produzido = total_produzido + pecas
    
    controle += 1

media_horas = total_produzido / quantidade_horas

print("Total produzido:", total_produzido)
print("Média por hora:", media_horas)