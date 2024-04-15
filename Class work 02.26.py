
import requests
'''
url = 'https://www.whenisthenextmcufilm.com/api'

response = requests.get(url)

if response.ok:
    as_text = response.text
    as_json = response.json()

    print(as_text)
    print(as_json)

    print(as_json['title'])
    print(as_json['overview'])
    print('   ')
    print(f"{as_json['title']} releases in {as_json['days_until']} days")
    print(f"Release date: {as_json['release_date']}")
    print(f"Production type: {as_json['type']}")
    print(f"Overview: {as_json['overview']}")

    print(f"Наступний фільм: {as_json['following_production']['title']}")

'''

address = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/'
first_url = f"{address}currencies.json"
currensies_response = requests.get(first_url)
currensies_list = list(currensies_response.json().keys())
print(currensies_list)
stop_program = 0
while True:
    currency_from = str(input('Перша валюта'))
    for i in range(len(currensies_list)):
        if currency_from == currensies_list[i]:
            break
        elif i == len(currensies_list) - 1:
            print('NOT CORRECT!!!!!!')
            stop_program = 1
            break
    if stop_program == 1:
        break
    currency_to = str(input('Друга валюта'))
    for i in range(len(currensies_list)):
        if currency_to == currensies_list[i]:
            break
        elif i == len(currensies_list) - 1:
            print('NOT CORRECT!!!!!!')
            stop_program = 1
            break
    if stop_program == 1:
        break

    amount = int(input('Скільки?'))

    url = f'{address}currencies/{currency_from}/{currency_to}.json'

    response = requests.get(url)

    if response.ok:
        as_json = response.json()
        rate = as_json[currency_to]

        print(f"{amount} {currency_from} = {round(rate * amount, 2)} {currency_to}")
