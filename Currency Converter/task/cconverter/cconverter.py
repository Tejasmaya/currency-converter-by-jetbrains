# write your code here!
import sys

import requests
import json
print('Use 3 letter for currency. eg: US Dollars: USD, EURO: EUR')
code = input('Input the Currency you want to convert: ').lower()
# params = dict()
res = requests.get(f'http://www.floatrates.com/daily/{code}.json')
data_str = res.text
data_json = json.loads(data_str)
# print(type(data_json))
# print(data_json)
cache = {}
if 'usd' in data_json and not code == 'usd':
    usd = data_json['usd']['rate']
    cache['usd'] = usd
if 'eur' in data_json and not code == 'eur':
    eur = data_json['eur']['rate']
    cache['eur'] = eur
# print(cache)
flag = True
while flag:
    xcng = input('Enter the Currency to which you want to Convert: ').lower()
    if not xcng.isalpha():
        flag = False
        sys.exit()
    amount = float(input('Enter Amount'))
    # print('Checking the cache...')
    # print(cache)
    if xcng in cache:
        print('Oh! It is in the cache!')
        if xcng == 'usd':
            usd = float(cache['usd'])
            print(f'You received {round(amount * usd, 2)} USD.')
        elif xcng == 'eur':
            eur = float(cache['eur'])
            print(f'You received {round(amount * eur, 2)} EUR.')
        else:
            rate = float(cache[f'{xcng}'])
            print(f'You received {round(amount * rate, 2)} {xcng.upper()}.')
    else:
        # print('Sorry, but it is not in the cache!')
        rate = data_json[f'{xcng}']['rate']
        cache[f'{xcng}'] = rate
        print(f'You received {round(amount * rate, 2)} {xcng.upper()}.')

