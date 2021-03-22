import main
import json

URL = 'https://zzzzzzzzzzzzzzzzzzzzzzzz11.myshopify.com'
EMAIL = 'zzzzzzzzzzzzzzzzzzzzzzzz@gmail.com'
PASSWD = 'sannix@2019'


def write_file(data, file_name='data.json'):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


cookies_dump = main.get_cookies(url=URL, email=EMAIL, passwd=PASSWD)
list_product = main.get_entity(url=URL, entity='products', cookies=cookies_dump, api_version='2021-01')

write_file(data=list_product, file_name='products.json')
