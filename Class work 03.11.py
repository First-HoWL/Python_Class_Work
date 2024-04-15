import random


def sort_list(message):
    while True:
        numb = [int(number) for number in input(message).split()]
        if not numb:
            print('Nothing')
        else:
            return numb


def input_yes_no(message='', rand=False):
    if rand:
        return[random.randint(-50, 50) for i in range(10)]
    while True:
        answer = input(message).lower()
        if answer in ('т', 'так', 'yes', 'y', '+', 'no', 'n', '-', 'ні', 'н'):
            return answer in ('т', 'так', 'yes', 'y', '+')
        else:
            print('Uncorrect!')


def bubble_sort(list, sortByGrowth):
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(len(list) - 1):
            if (list[i] > list[i + 1] and sortByGrowth) or (list[i] < list[i + 1] and not sortByGrowth):
                list[i], list[i + 1] = list[i + 1], list[i]
                is_changed = True
    return list

def fsum(list):
    fsumansw = int(0)
    for i in range(len(list)):
        fsumansw += list[i]
    return fsumansw


def kilkst_paznix_chisel(list):
    dodatn = 0
    videmnix = 0
    parnix = 0
    neparnix = 0

    for i in range(len(list)):
        if list[i] >= 0:
            dodatn += 1
        elif list[i] < 0:
            videmnix += 1
        if list[i] % 2 == 0:
            parnix += 1
        elif not list[i] % 2 == 0:
            neparnix += 1
    print(f'додатніх: {dodatn}')
    print(f'від\'ємних: {videmnix}')
    print(f'парних: {parnix}')
    print(f'непарних: {neparnix}')


def peregortae_chisla(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[len(list) - i - 1])
    print(new_list)


def poisk_v_liste(list, chykaimo):
    for i in range(len(list)):
        if list[i] == chykaimo:
            return True
    return False

def factorial_chisla(list):
    new_list = []
    for i in range(len(list)):
        a = 0
        for _ in range(list[i]):
            print(_)
            if _ != 0:
                a += (int(list[i]) * _)

        new_list.append(a)
    return new_list



# numb = sort_list('Введіть списо чисел через пробіл')
# sortByGrow = input_yes_no('Ви чочете відформатувати список за зростанням? (т/н)')
# bubble_sort(numb, sortByGrow)
# print(f'{numb}')
#


'''
1

print(fsum(sort_list('Введіть списо чисел через пробіл: ')))

'''
'''
2
print(bubble_sort(sort_list('Введіть списо чисел через пробіл: '), False)[0])
'''
'''
3
kilkst_paznix_chisel(sort_list('Введіть список чисел через пробіл: '))

'''
'''
4
peregortae_chisla(sort_list('Введіть список чисел через пробіл: '))
'''
'''
5
print(poisk_v_liste(sort_list('Введіть список чисел через пробіл: '), 5))
'''

print(factorial_chisla(sort_list('Введіть список чисел через пробіл: ')))
