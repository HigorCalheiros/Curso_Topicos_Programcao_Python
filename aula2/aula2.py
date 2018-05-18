'''

    Autor: Higor Calheiros
    Data: 18/05/2018 - RJ

    Este programa calcula uma soma ou multiplicação entre dois números

'''

n1=float(input("Digite um valor: "))
n2=float(input("Digite mais um valor: "))

opcao=(input("Digite s para somar e m para multiplicar:" ))

soma=n1+n2
mult=n1*n2

if opcao=='s' or opcao =='m':

    if opcao=='s':
        print(f"Resposta: {soma}")
    else:
        print(f"Resposta: {mult}")
else:
    print(f"Opcao não válida")



