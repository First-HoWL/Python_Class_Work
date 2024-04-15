'''
i = int(0)
spisokocenok = []
while True:
    a = input('numbers')
    if a == 'exit':
        break
    elif a.isdigit():
        if int(a) > 12 or int(a) < 1:
            print('NOT CORECT!!!')
        else:
            spisokocenok.append(int(a))
    else:
        print('NOT CORECT!!!!!!!!')
print(spisokocenok)
print('Середньоарефметичне:', int(sum(spisokocenok)) / len(spisokocenok))
'''

import random

a = [random.randint(-20, 20) for i in range(20)]
print(a)
videmni = []
parni = []
neparni = []
i = 0

for i in range(len(a)):
    if a[i] < 0:
        videmni.append(a[i])
print(videmni, '=',sum(videmni))

for i in range(len(a)):
    if a[i] % 2 == 0:
        parni.append(a[i])
print(parni, '=',sum(parni))

for i in range(len(a)):
    if not a[i] % 2 == 0:
        neparni.append(a[i])
print(neparni, '=',sum(neparni))
