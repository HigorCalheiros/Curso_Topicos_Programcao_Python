'''def hello():
    print ('Hey')
    print ('Ho')
    print ('Lets go')

hello();
hello();
hello();



'''


'''def hello(name):
    print(f'Hello {name}')

hello('Higor')'''

''' Calculo da area de um triangulo usando função'''
'''
def areatriangulo(base,altura):
    area=(base*altura)/2
    print(f"Area do triangulo: {area}")


base=float(input('Insira a base do triangulo: '))
altura=float(input('Insira a altura do triangulo: '))

areatriangulo(base,altura);

'''

'''import random

def getNumber(number):
    if number == 1:
        return 'eh o numero 1'
    elif number == 2:
        return 'eh o numero 2'
    elif number == 3:
        return 'eh o numero 3'
    elif number == 4:
        return 'eh o numero 4'
    elif number == 5:
        return 'eh o numero 5'
    elif number == 6:
        return 'eh o numero 6'
    elif number == 7:
        return 'eh o numero 7'
    elif number == 8:
        return 'eh o numero 8'
    elif number == 9:
        return 'eh o numero 9'

r = random.(1,9)
sorteio=getNumber(r)
print(sorteio)'''

'''Funcao Recursiva'''

def fatorial(numero):

    if numero ==0 or numero==1:
        return 1
    else:
        return numero*fatorial(numero-1)

x=int(input('Digite um numero para calcular o fatorial: '))
res=fatorial(x)
print(f"O fatorial de {x} eh {res}")

