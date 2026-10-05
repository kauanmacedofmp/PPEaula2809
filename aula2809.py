'''
from time import sleep

cR = 10

#para cada var i na sequencia que inicia em 1 e vai até 10
for i in range(1, 11):
    print(cR)
    cR = cR - 1 #cR -= 1
    sleep(1)

print('felix anu novu')
'''

'''
from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
'''

'''
soma = 0

#para cada i na sequência que inicia = 1 e final = 500
for i in range (1, 11):
    soma = soma + i

print(soma)
'''

'''
somapar = 0
somaimpar = 0
somatres = 0

#para cada i na sequência que inicia = 1 e final = 500
for i in range (1, 11):
    if i % 2 == 0:
        somapar = somapar + i

    elif i % 2 == 1:
        somaimpar = somaimpar + i
    
    if i % 3 == 0:
        somatres = somatres + i

print(somapar)
print(somaimpar)
print(somatres)
'''

'''
num = int(input('Digite um número de 1 a 10: '))

soma = 0

#para cada i na sequência que inicia = 1 e final = 500
for i in range (1, 11):
    if i % num == 0:
        soma = soma + i

print(soma)
'''