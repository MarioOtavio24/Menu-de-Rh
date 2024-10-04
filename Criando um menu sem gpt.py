import os
os.system ('cls')
RH=[]
while True:
    operação=input('''==================================================
                (1) incluir
                (2) relatório geral
                (3) sair
 =================================================> ''')
    if operação=='1':
        matricula=input("entre com a matricula ")
        nome=input("entre com o nome ")
        salário=float(input ("entre com o salário "))
        RH.append ([matricula,nome,salário])
        input("Inclusão foi feita com sucesso, precisone enter para voltar o menu")
    elif operação=='2':
        print(RH)
    else:
        operação=='3'
        print("fim do programa")
        break
    