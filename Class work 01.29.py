'''
1
a = int(input('1 число'))
b = int(input('2 число'))
print(list(range(a, b)))



альтернатива


a = int(input('1 число'))
b = int(input('2 число'))
b = b + 1
while print(list(range(a, b))):
    if range == b:
        break


'''



'''

2

a = int(input('1 число'))
b = int(input('2 число'))

if a % 2 == 0:
    a = a + 1
print(list(range(a, b, 2)))



альтернатива


a = int(input('1 число'))
b = int(input('2 число'))
b = b + 1
if a % 2 == 0:
    a = a + 1
while print(list(range(a, b, 2))):
    if range == b:
        break

'''







'''

3

a = int(input('1 число'))
b = int(input('2 число'))
b = b + 1
if a % 2 != 0:
    a = a + 1
print(list(range(a, b, 2)))


альтернатива


a = int(input('1 число'))
b = int(input('2 число'))
b = b + 1
if a % 2 != 0:
    a = a + 1
while print(list(range(a, b, 2))):
    if range == b:
        break

'''


'''
4
a = int(input('1 число'))
b = int(input('2 число'))
for i in range(b, a, -1):
    print(i, end = ' ')
    

альтернатива


a = int(input('1 число'))
b = int(input('2 число'))
while print(list(range(b, a, -1))):
    if range == a:
        break
'''


'''

5

a = int(input('1 число'))
b = int(input('2 число'))

if b < a:
    a, b = b, a

if a % 2 == 0:
    a = a + 1
for i in range(a, b, 2):
    print(i, end = " ")


альтернатива


a = int(input('1 число'))
b = int(input('2 число'))

if b < a:
    a, b = b, a
else:
    b = b + 1
if a % 2 == 0:
    a = a + 1
while print(list(range(a, b, 2))):
    if range == b:
        break
'''
