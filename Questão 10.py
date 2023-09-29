#QUESTÃO 10

#entradas
gender = str(input('Digite F/M para feminino ou masculino, respectivamente. Ou digite O para outro: '))

#processamento e saídas
if(gender == 'F' or gender == 'f' or gender == 'Feminino' or gender == 'feminino'):
    print('Você se identifica do sexo feminino.')
if(gender == 'M' or gender == 'm' or gender == 'Masculino' or gender == 'masculino'):
    print('Você se identifica do sexo masculino.')
if(gender != 'F' and gender != 'f' and gender != 'M' and gender != 'm' and gender != 'Feminino' and gender != 'feminino' and gender != 'Masculino' and gender != 'masculino'):
    gender = str(input('Digite qual sexo você se identifica: '))
    print(f'Você se identifica do sexo {gender}.')