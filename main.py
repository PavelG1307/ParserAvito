import requests
import csv
import json
import sys

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
cookie = 'u=2ospkoq5.q3xuox.7fs4jiv87n4; buyer_local_priority_v2=0; _ym_uid=1623759258873598042; sessid=5887d4513ea2d827c428b3d9b8dc93ad.1626951703; _ym_d=1641900929; __gads=ID=62e4b90be5a4d21a:T=1625657273:S=ALNI_MYDSgTp12uCkXfw-7HFLriUehI8TQ; adrcid=AdN-BkbrhKDUxXDsFGH8omQ; tmr_lvid=b8ddbd48e59db7c09ea3e12b1ba5e547; tmr_lvidTS=1653044851924; _gcl_au=1.1.1656198276.1653987768; buyer_location_id=637640; buyer_laas_location=637640; _ym_isad=2; _gid=GA1.2.1553517392.1657627701; f=5.9fd3735f16182a28b32428cf8e3c6b5047e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b99364cc9ca0115366433be0669ea77fc074c4a16376f87ccd915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d4047e992ad2cc54b8aa8c772035eab81f5e1e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca746b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba4604438f9f51f7fb331d49c1c93fcdfd7461c4c4543acfc7034638ec26cf48d72d17c7721dca45217ba1938a91a59ce5e68f97af514fc92d30e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa410b4b42af931ca18edb85158dee9a662da10fb74cac1eabb3ae333f3b35fe91de6c39666ae9b0d73339614c6f29137599c7f25537e9455a; ft="rPIYWUMAhsBO7vHyWe3pzwAspfLHaMngksgux4AC7MRzIUAOOy8RCs0IAwm5zWhAQF2hQmzCNJn3UGPR0/qofmPygDsr25JArSjABvQui4eSKqnEltcUYMSmqy22SuNR5WOY0lHjZAkw0gHKBhRnksYYvMkIEi8mvPpyVu3V44ODvqIwPkSJ/utNDMUcGz8G"; uxs_uid=54224b80-01dc-11ed-abeb-090cbed4b192; __ddg1_=Kr3srU2vCr43yNfdkN36; luri=moskva; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISWtQdTBhVzcyRHpGR3NKSHVJWTBqVktoSlQyVXBudTdSandaaktOc0YwV0tuUjZwMzZlNVpjR01mNjVsTTJHc3FHZmNHOVdJWHV0R2VPRjVrRXhwSDcxRk9UMzdCZUdJSDZUNEI3blVzNGVKSUszR3NVNTVkc1dsSE9vVjFudXdhdzBrN0t2VlRYckhlWHlSWDhJMGxuK3U5Ymk0MjBGbkNTMlBOY3FaVWpia1Q3Z0RWVW9tL1I4QW5DRWhXWktnV1ZjR1lQM2k4aGF2cVdvWUNnNEQ1M2hmeThlOEFJWTZIUlAxWU84RnpIaWhDWWswV2pjQ3M4Yk1ydXBIcHJIbk9IMkV1NTBsSW5XMkZBZmhWR0RxTEM0VC9taytIblhiRHBuVFdwNnJ4cjV3VjJ4cUVNM3lPbjJSRThodHRMYXhYYnN3WGdKWE4wNnZFTmRqd1RtYmRJbHlubXN6VE9WbjRNZWg5WVd4RVFDQWZqK3R3OHhUQnJMSVFPRUNtOE55MXZER3AzNWlET2orQ1UvcjdURHQ2VjhiaXViMFNaSEh2Wng4di9OTzdkc1pTdUNuMTIzKzk4bTVkeC9rN1VXTHVTblQ3elZKQit6Q2NXUmUxY3ppaTI0dWs2TGZWUEUzSFBKTUpIbzdJTE9QWVFUbXhyRjBLVldVdXJKc2NVMGo4NWpxVFFORXltZllzOCtoeUhyalpsRFpkdzJvOWJrSTVYSy9rbVVTQWVhc2JvVGY1K2hpZ0JsTDZkL1dhMVlFaFpQSDgxcHlTeTBXU2dWYmRIK21odHV1eXR4RDFTUzNHUFIxWWNlejQySkllWHhjbDVYdlZqRVRjWVE4aWlIS1dRQVkzeW5sSTBWZXNGYW40Yis3Y2NsOWMrTFZqTzVRNEhTeEZkVGcwNlZPQTlFaXIwYjdySm51RTRQN3lwOVBLTG9hOHpPREI4NFpaQmlRdjVBNTBvVGtCdHVyQnk0NTR1OGFHaW0yYm9Dckl2RkhyZmpoMEJ1RmNYbE4zNEhkT0FCVVl4SUZtc1g1OUg0dVJva2FodFl5VWtmc05GYUFqZnlZQnd6Q3BXSGd1R0JqVE1wYU1uWWtHNkRxRWRFcithaC9WREg1TzdhQjczSmxtd2pncWhQNmRudVluL0wwdzcrZ3BwTzRDQkhSczFaSXoxNU5qYmxzZlE5cTF6cmlZVFBwdm5EM1BCTUExWFY5czlmTmRFMTZUSEdTSzJUQ01Va05EcWh2Wm1tVzFpTzI1c0k2RXlMTWM0SmsrQkw1RzhZSWZVWDhTTDZBelVUMU95dmR4TyIsImlhdCI6MTY1NzYzMDg5MSwiZXhwIjoxNjU4ODQwNDkxfQ.tZrgR-ddiPR84i9At68Tabnp9kAzIa-gcYkIhsMlWYg; _ym_visorc=w; v=1657632306; redirectMav=1; sx=H4sIAAAAAAAC%2F5zSSZKjMBCF4buwZqFUaqzbaDbIILDM2MHdO7xwhb2tC3zxK%2FX%2BNURjBGuMEUYRi4qiF4RSo5VHGj02P%2F%2BatflpqCv7Rud0pOKO6bkfe0eyXHZJce66R9M2ofkBwaUErQm92oYRVIyBJFFHzrWgVlJJNBpExazTb1meNub5uZBY%2FHLrPLuf9SScx%2BkwroufsqSor7bhSnuUxgMlStEIXgOA5DTyGK00v839nnOkZ9%2F7OUQR7byYwIvEuz36s5%2B%2BmpViL7mMpsiAbku1pJyLYmVLxdU3OUTZWxjqBDYBS924Au%2BB66GyPajlKxbUK1YIIZyXImqhuWBCB2kDai85cU763zOMEJd%2BPhPxGrbx6LW%2F96fGdch6evBPmRKkcLWN8hoCtZSisFw6GnUMTEUFjhBg6N7yrVvXM7HFbwDMgA1kC7V7kPG8P4d7%2FjqDlOpqGz2w%2BbGOa5gqcTnnXFUptar0Jm1az20LPAygt64cI0mYhIbHgz9V2D5JxilebWPzMekZl7kqV3LOLmdSSmXsd2DLMrqbNIcY1zR2w3SrZx86DtIMa%2Bw%2BSUXxNTBXXFBPJfzrjypLr8iSS61%2FqUQQV9t4wYV10hkuhdPBkBCUCcIwKrxRQr3lO2oyb%2F6IO6uVHhn9WAPdp5MwPt%2FO7%2FcjudomOhHQMWMYtzoEBOKVi5xQzjil4P%2FSDAyv638AAAD%2F%2F4pO1YvDAwAA; _mlocation=637640; _mlocation_mode=laas; _ga=GA1.2.418341391.1625657273; tmr_detect=0%7C1657633935657; tmr_reqNum=203; _ga_9E363E7BES=GS1.1.1657627701.64.1.1657633957.19' \

search = 'склад'
categoryId = 42
locationId = 637640
sort = 'priceDesc'
withImagesOnly = 'false'
limit_page = 50

s = requests.Session()

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
s.get('https://m.avito.ru/')                    # Делаем запрос на мобильную версию.
url_api_9 = 'https://m.avito.ru/api/11/items'    # Урл первого API, позволяет получить id и url объявлений по заданным фильтрам
                                                # Тут уже видно цену и название объявлений
params = {
    'categoryId': categoryId,
    'params[536]': 5546,
    'params[554]': 5727,
    'locationId': locationId,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1610905380,
    'display': 'list',
    'limit': limit_page,
    'query': search,
}

params['key'] =  key


def getIDS(f):
    ids = []
    cicle_stop = True       
    cikle = 0               
    items = []             
    while cicle_stop:
        cikle += 1
        print(f'Страница: {cikle}')
        params['page'] = cikle
        res = s.get(url_api_9, params=params)
        try:
            res = res.json()

        except json.decoder.JSONDecodeError:
            cicle_stop = False
            break

        if res['status'] != 'ok':
                print(res)
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
        for item in items:
            if item['type'] == 'item':
                ad_id = str(item['value']['id'])
                ids.append(ad_id)
                f.write(str(ad_id) + '\n')
    return ids


def getInfo(id):
    url_info = f'https://m.avito.ru/api/18/items/{id}'
    params = {
        'key': key
    }
    info_js = s.get(url_info, params=params).json()
    if not 'error' in info_js:
        return info_js
        # f = open('test.json', mode = 'w')
        # json.dump(info_js, f)
    else:
        print(info_js)
        

# additionalSeller.parameters
['Тип здания', 'Класс здания', 'Общая площадь', 'Этаж', 'Отделка', 'Залог', 'Комиссия, %', 'Категория', 'Парковка', 'Тип парковки', 'Отдельный вход','Общая площадь','Аренда части площади','Высота потолков, м','Включено в стоимость','Отопление','Отделка','Вход','Отдельный вход']
def ParseInfo(info):
    title = info['title']
    address = info['address']
    lat = info['coords']['lat']
    lng = info['coords']['lng']
    description = info['description']
    url = info['sharing']['url']
    time = info['time']
    price = info['price']['value']
    images = info['images']
    images_arr = []
    name_company = info['seller']['name']
    name_manager = info['seller']['manager']
    postfix = info['seller']['postfix']
    additionalSeller = info['additionalSeller']['parameters']
    for parameter in additionalSeller:
        title_p = parameter['title']
        description_p = parameter['description']
        print(f'{title_p} - {description_p}')
    
    for image in images:
        images_arr.append(image['1280x960'])

    parameters = info['parameters']['flat']
    for parameter in parameters:
        title_p = parameter['title']
        description_p = parameter['description']
        print(f'{title_p} - {description_p}')
    user_hash = info['seller']['userHash']
    url_seller = f'https://www.avito.ru/user/{user_hash}/profile'
    print(url)

def SaveInfo(info):
    csvFile = open('example2.csv', 'a')
    with csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(info)


def main():
    # f = open('ids.ino', mode = 'a')
    # ids = getIDS(f)
    # print(f'Всего объявлений: {len(ids)}')
    f = open('ids.ino', mode = 'r')
    ids = f.readlines()
    for i in range(len(ids)):
        info = getInfo(ids[i].strip())
        ParseInfo(info)
    # SaveInfo([[]])
    # f = open('test.json', mode = 'r')
    # info = json.load(f)
    # ParseInfo(info)

if __name__ == '__main__':
    main()



# https://m.avito.ru/api/18/items/2448175824?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&action=view&context=H4sIAAAAAAAA_xTKUcrDIAwA4LvkBGnUYtPD_KjR9h8ykHRoN3b34dv38AUm_igvDAN2ZTNxDq1Xye2_v1rVfru7t8f5tk9TD7SzOYbxp8c1bZHBGh83kmKSUHKbjyjBJ6GckbDEdQnZ0ZoE9u8vAAD___YojBJxAAAA
####################################################################
# params = {'key': key}
# for i in items: # Теперь идем по ябъявлениям:
#     ad_id = str(i['value']['id'])
#     # url_more_data_1 = 'https://m.avito.ru/api/1/rmp/show/' + ad_id  # more_data_1 = s.get(url_more_data_1, params=params).json() # Тут тоже моного информации, можете посмотреть
#     url_more_data_2 = 'https://m.avito.ru/api/15/items/' + ad_id
#     more_data_2 = s.get(url_more_data_2, params=params).json()
#     if not 'error' in more_data_2:
#         # print(more_data_2)            # В more_data_2 есть всё, что надо, я вывел на принт наиболее интересные для наглядности:
#         print(more_data_2['title'])
#         print(more_data_2['price'])
#         print(more_data_2['address'])
#         url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
#         phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
#         if phone['status'] == 'ok': phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1]) # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода)))
#         else: phone_number = phone['result']['message']
#         print(phone_number)
#         print(more_data_2['seller'])
#         # print(more_data_2['description']) # Скрыл, т.к. много букв
#         print('=======================================================\n')


