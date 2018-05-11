'''
Este programa transforma o valor total de segundos em horas, minutos e segundos
'''

segundos = int(input('Insira o total de segundos:'))

horas=segundos//3600
minutos=(segundos%3600)//60
seg = (segundos%3600)%60

print(f" \n {horas} hrs : {minutos} min : {seg} seg")

