'''
    Autor: Higor Calheiros
    Data:18/05/2018

    Este programa mostra se o aluno está reprovado ou nao
'''

freq=int(input("Informe , em porcentagem, a frequência do aluno: "))


if freq>=75 and freq<=100:
    media=float(input("Informe a media do aluno de 0 a 10: "))

    if media>=7 and media<=10:
        print(f"O aluno está aprovado com {media} de média")

    elif media>=3 and media<7:

        print(f"O aluno esta de PF \n")
        mediapf=float(input("Informe a media da PF: \n"))
        mediafinal=(media + mediapf) / 2

        if mediafinal>=5 and mediafinal<=10:
            print(f"O aluno esta aprovado com {mediafinal} de média final! ")

        elif mediafinal>=0 and mediafinal<5:
            print(f"O aluno esta reprovado com {mediafinal} de média final ! ")

        else:
            print(f"Valor incorreto!")

    elif media>=0 and media<3:
        print(f"O aluno está reprovado direto com {media} de média!")

    else:
        print(f"Valor incorreto!")


elif freq>=0 and freq<75:
    print(f"O aluno esta reprovado por falta com {freq}% de frequência!")

else:
    print(f"Valor incorreto!")




