while True:
    spisok = 'products.txt'
    with open(spisok, mode='r', encoding='utf8') as file:
        products = file.read().split('\n')
    number = 1
    menu = int(input('Що ви хочете зробити(1 - Переглянути записи, 2 - видалити запис, 3 - Додати запис, 0 -вийти): '))
    if menu == 0:
        break
    elif menu == 1:
        with open(spisok, mode='r', encoding='utf8') as file:
            print("Записи:")
            for product in products:
                if product not in ['']:
                    print(f"{number}. - {product}")
                    number += 1
    elif menu == 2:
        with open(spisok, mode='w', encoding='utf8') as file:
            delete_zap = (int(input('Який запис видалити'))) - 1
            products.pop(delete_zap)
            file.write('\n'.join(products))
    elif menu == 3:
        with open(spisok, mode='w', encoding='utf8') as file:
            zap = input('Ваш запис: ')
            products.append(zap)
            file.write('\n'.join(products))
    else:
        print('Not correct!')
