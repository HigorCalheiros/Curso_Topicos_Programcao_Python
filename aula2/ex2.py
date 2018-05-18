'''
    Autor: Higor Calheiros
    Data:18/05/2018

'''

preço=int(input("Informe qual o preço do produto em reais: 10, 15, 25, 30 ou 40 \n"))

if preço==10:
    print(f"O produto é da categoria 1")
elif preço==15:
    print(f"O produto é da categoria 2")
elif preço==25:
    print(f"O produto é da categoria 3")
elif preço==30:
    print(f"O produto é da categoria 4")
elif preço==40:
    print(f"O produto é da categoria 5")
else:
    print(f"O Preço selecionado não é válido!")
