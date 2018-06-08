'''Higor Calheiros 08/06/2018

1 1 2 3 5
    Sequencia de Fibonacci'''

def fibonacci(x):

    if x==1:
        return 1
    else:
        return x+fibonacci(x-1)
x=int(input('Digite um valor para calcular a sequencia de fibonacci: '))

res=fibonacci(x)
print(res)

'''meuPassaro={'cor':'amarelo', 'tipo': 'calopsita', 'tamanho': 'pequeno'}

print(meuPassaro['cor'])
print('Meu passaro eh uma '+ meuPassaro['tipo'])
'''

'''itensMercado={'fruta': 'maça', 'laticínio': 'iogurte', 'bebida': 'suco', 'proteína':'frango'}

print ('frango' in itensMercado.values())
print ('bebida' in itensMercado.keys())'''



'''Desafio RPG'''

'''displayInventory={'rope':1, 'torch':6, 'gold':42, 'dagger':1, 'shield':1}

x = list(displayInventory.values())
print (x)
a=x[0]
b=x[1]
c=x[2]
d=x[3]
e=x[4]

total=(a+b+c+d+e)

print('Inventário:')
print (f"rope: {a} \ntorch: {b} \ngold: {c} \ndagger: {d} \nshield: {e}")
print (f"Total de itens: {total}")


'''




