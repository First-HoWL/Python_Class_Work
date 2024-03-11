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

def fsum(list):
    fsumansw = int(0)
    for i in range(len(list)):
        fsumansw += list[i]
    return fsumansw



# numb = sort_list('Введіть списо чисел через пробіл')
# sortByGrow = input_yes_no('Ви чочете відформатувати список за зростанням? (т/н)')
# bubble_sort(numb, sortByGrow)
# print(f'{numb}')
#


'''
1

print(fsum(sort_list('Введіть списо чисел через пробіл: ')))

'''

print(bubble_sort(sort_list('Введіть списо чисел через пробіл: '), True)[0])

