#QUESTÃO 9

#entradas
numero = float(input('Digite qualquer valor: '))

#processamento e saídas
if (numero < 0):
    print('O valor é negativo')
elif(numero == 0):
    while(numero == 0):
        numero = float(input('Digite um valor diferente de zero: '))
    if(numero < 0):
        print('O valor é negativo')
    else:
        print('O valor é positivo')
else:
    print('O valor é positivo')