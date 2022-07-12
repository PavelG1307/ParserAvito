import requests, json, sys

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = 'u=2fkcz6l8.1kgj55.g3xn3vc0t3; _ym_uid=1560267406178859309; buyer_selected_search_radius4=0_general; buyer_selected_search_radius3=0_services; buyer_selected_search_radius2=0_job; buyer_selected_search_radius0=200; buyer_local_priority_v2=0; buyer_index_tooltip=1; sessid=2a3bf282b493b187df5d8dc23306e145.1626537433; auth=1; buyer_laas_location=652430; _gcl_au=1.1.733197779.1652816764; v=1657654463; luri=moskva; _ym_d=1657654472; _ym_isad=1; tmr_lvid=5c9c483ac660d500846a4d65251b749d; tmr_lvidTS=1657654489421; _gid=GA1.2.2632564.1657654490; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa858f6718e375efe9248bdd0f4e425aba7085d5b6a45ae867378ba5f931b08c66a72a0378f24244a7a2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabf8e5e9b21a40e18dde87ad3b397f946b4c41e97fe93686adf74ad50eaa2b3372f415355acea9907602c730c0109b9fbb551b50768d5f707e6f9088c33a557ef70e28148569569b7903532f306346f575b9e8022cece544b32ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd74801d2e1440f9b5e4f3de19da9ed218fe23de19da9ed218fe2ddb881eef125a8703b2a42e40573ac3cd81d609ad4115c32bcdb5a5dea4d64cf; ft="4GDrFjTQl5E6tNlykiW1h6a0Clle3t6gkc53Ehj8v2y1ET6ospzoFOy7dn8fB7Q5ynjtpHR3ixYRr9hSVDGMQ0VWF/8Aj1WC46DJue9Xzl/lDZwauU413MCpVeR1MlqodYHJIwCzSLnD12o9lSmk00AXQQWiaYq6ALPFaLyt0iZIBbLKdHLmuFMvXt8GdaDX"; buyer_location_id=637640; sx=H4sIAAAAAAACA53Ry7LCIBAE0H9h7YLHDAz+DQyEJJj4iCWJlv9+cxcu3LrvOtVd/RLGIWkJEqlDFSFwcp02mgxxTk5ZcXyJhziKp79hbO1ZN760c6Q883QZT4bv0a3tKg4ii6Oy6ByonXsfhCMVbZaUHaHJCbFjK1OnkzSI0aaPPNK0xOl2jafxrm4LwH0Y6gBgWV85rt+ytrvsvZfeQNoTHBwktlolrYxWTnki/MiUzqq1SdPjsj2hVWClpl7lsnXRNP0tG9hl7uZ13LKOp9oWya0uRZ6XAsuHDHK8bGw2Sg0fs+3ptI629qGYvr+FL1J6/182WbSRHQd0ln0OMmcK2QbQNgWy9JOs1S5n3KfNa81whlIYZClQABr/RKLbyaHW2M3T8Fi5UKH9SOal8PLTV2je7z+HiQ8ZYQIAAA==; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISkRoNkVQZGMzaUhBVjc3QlpVWDhYMG4xS0NKYklyeGVJZkVmSW9SL1FyRDI2dHVKY0dRQzNHODh2WVY5QjNGSWoyOURTOGhvZ2xaM1J5SUNlM3lpOXpuYzZXK0xGcGt3S1o4WmtabTdLT2dJSUFOajFsMzZhQjIyQXRNd1ZPeXZDR1RZRWVsYmtpT1k5TnJPdnE2enpTNzlDakZqTEM2b3JDTE1wNG4xUnl4eDdEQmZEWEpZTDJMZyt0WVZacm1EWjlZeFlxL3BIUEFjSDlBQjhoQmpVUmNKYzF0Qlc4TXhSUTNqUFN1cDBCYmpORUs3YmN1WHlQU0dyenZNdFgvSUk5bHpkN1RZOW9hb2UrVXVGQmhrMlg2ZVdwRUFGK3ZVUjZQYkxJME5zdmxoV3Q3c0p2OUp5eXNPdUZHNE5HVXYvZ1VkRDN2bjh2ZE9aeXNFeHFMNnB2cXVBd28wQXc1dm95cHZQNFcvYXVualNnd0pvWk5GVGZTWHRGY3BUVURXODhDaG9rNVh1U1NBWWU1QnMzWEVDMkYxdUs2K3ZXalRNQnVMTjNCMnFxSXA1N21LLzNYV1ZQcmlVeVBNTS8wN0ZaSXgwUHFwM3Q4bHBFQlh0dGNxdnNPNGhuSGhQRmJVVC94cVZ1OFhXQXYzTHpBZ1hSc3ozL0hKdXFYdGk0OGhzUEVpbkRrMlF0ZDJHNmx2QjJYNzlYRk1WVlc0MmtCWmgvaERQL0JqSjV4aTZTeVdSTEhLS1c5Q2dOcjJQWXpFVE00eW9CbUV6c2VEREtGT3lSQ2NxR25waCtyTGJsa2w0SHlOM2hQMTZWTENxb1g4NXZFUlJ1Tm9QbWYrTHlIcVB2TG9NODEvVVBHdGduU1puakJhWHE2M3FsU0pqcVJ0SjFOc0kwMXVIRzlOb0J4eSt6M3pudXN3MzVacWVFd1BiL2hiYmV5TldlTFlOZ1BxZ0FVdXl3Z2tMSWlMU3pJamVTZEZ4U05weWRBVDArRllWZFU5eWR5Zy9KTjhxaWFSVEtNSjhxY09ZSWhPS2hXdzdzQ3RHYkpZVTVoVHNoZVNidUticElCUVhYb0hDZzVFbGUzRmJLMVBDUUR3YUl5YkdHQmRYdEVWOVFXZHNZa3F3NjZoU0l5ek9iRGs2NVQzd29GelpsVzBHQTUzMWRxd21maW1qSWY2Smdxalg0M1hvMk43c1JPeTMycUxWdEY3QzNGajVmMUVhWkF3WHl6d3VOeUI5Y1I2bkM3aDdsajRMbTB4NU82Y0pqcnNCTFd3WVRFLzAzbjlnT0JvWk1yM3d3WlYyQiIsImlhdCI6MTY1NzY1NzgwNCwiZXhwIjoxNjU4ODY3NDA0fQ.u0ImCa7ThsN2Rdsil-cWSumjBAxXfzbYo1UpCEV03g4; _mlocation=637640; _mlocation_mode=laas; uxs_uid=a2c18040-0221-11ed-87ea-93fc87eb159f; _ga=GA1.2.1264586811.1652816766; tmr_detect=0|1657659080835; dfp_group=14; _dc_gtm_UA-2546784-1=1; tmr_reqNum=35; _ga_9E363E7BES=GS1.1.1657657753.4.1.1657660196.49' \
# Если забанили, то добавьте свои куки, это не боевой код но он делает то, что надо
search = 'suzuki+gsx-r'     # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = 14
locationId = 641780         # Новосибирск
searchRadius = 200
priceMin = 200000
priceMax = 450000
sort = 'priceDesc'
withImagesOnly = 'true'     # Только с фото
limit_page = 50     # Количество объявлений на странице 50 максимум

def except_error(res): # Эту функцию можно дополнить, например обработку капчи
    print(res.status_code, res.text)
    sys.exit(1)

s = requests.Session()                          # Будем всё делать в рамках одной сессии
# Задаем заголовки:
headers = { 'authority': 'm.avito.ru',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9',}
if cookie:                                      # Добавим куки, если есть внешние куки
    headers['cookie'] = cookie
s.headers.update(headers)                       # Сохраняем заголовки в сессию
print(s.get('https://m.avito.ru/').text)                 # Делаем запрос на мобильную версию.
url_api_9 = 'https://m.avito.ru/api/9/items'    # Урл первого API, позволяет получить id и url объявлений по заданным фильтрам
                                                # Тут уже видно цену и название объявлений
params = {
    'categoryId': 14,
    'params[30]': 4969,
    'locationId': locationId,
    'searchRadius': searchRadius,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'params[110275]': 426645,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1610905380,
    'display': 'list',
    'limit': limit_page,
    'query': search,
}
cicle_stop = True       # Переменная для остановки цикла
cikle = 0               # Переменная для перебора страниц с объявлениями
items = []              # Список, куда складываем объявления
params['key'] =  key
while cicle_stop:
    cikle += 1          # Так как страницы начинаются с 1, то сразу же итерируем
    params['page'] = cikle
    res = s.get(url_api_9, params=params)
    try:
        res = res.json()
    except json.decoder.JSONDecodeError:
        except_error(res)
    if res['status'] != 'ok':
            print(res['result'])
            sys.exit(1)
    if res['status'] == 'ok':
        items_page = int(len(res['result']['items']))

        if items_page > limit_page: # проверка на "snippet"
            items_page = items_page - 1

        for item in res['result']['items']:
            if item['type'] == 'item':
                items.append(item)
        if items_page < limit_page:
            cicle_stop = False
####################################################################
params = {'key': key}
for i in items: # Теперь идем по ябъявлениям:
    ad_id = str(i['value']['id'])
    # url_more_data_1 = 'https://m.avito.ru/api/1/rmp/show/' + ad_id  # more_data_1 = s.get(url_more_data_1, params=params).json() # Тут тоже моного информации, можете посмотреть
    url_more_data_2 = 'https://m.avito.ru/api/15/items/' + ad_id
    more_data_2 = s.get(url_more_data_2, params=params).json()
    if not 'error' in more_data_2:
        # print(more_data_2)            # В more_data_2 есть всё, что надо, я вывел на принт наиболее интересные для наглядности:
        print(more_data_2['title'])
        print(more_data_2['price'])
        print(more_data_2['address'])
        url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
        phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
        if phone['status'] == 'ok': phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1]) # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода)))
        else: phone_number = phone['result']['message']
        print(phone_number)
        print(more_data_2['seller'])
        # print(more_data_2['description']) # Скрыл, т.к. много букв
        print('=======================================================\n')