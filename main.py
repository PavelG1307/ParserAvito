from http import cookies
import requests
import csv
import json
import sys
import time


key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
search = 'склад'
categoryId = 42
locationId = 637640
sort = 'priceDesc'
withImagesOnly = 'false'
limit_page = 50


def raiseSession():
    s = requests.Session()
    cookie = 'u=2ospkoq5.q3xuox.7fs4jiv87n4; buyer_local_priority_v2=0; _ym_uid=1623759258873598042; sessid=5887d4513ea2d827c428b3d9b8dc93ad.1626951703; __gads=ID=62e4b90be5a4d21a:T=1625657273:S=ALNI_MYDSgTp12uCkXfw-7HFLriUehI8TQ; adrcid=AdN-BkbrhKDUxXDsFGH8omQ; tmr_lvid=b8ddbd48e59db7c09ea3e12b1ba5e547; tmr_lvidTS=1653044851924; _gcl_au=1.1.1656198276.1653987768; buyer_location_id=637640; buyer_laas_location=637640; _gid=GA1.2.1553517392.1657627701; uxs_uid=54224b80-01dc-11ed-abeb-090cbed4b192; __ddg1_=Kr3srU2vCr43yNfdkN36; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISWtQdTBhVzcyRHpGR3NKSHVJWTBqVktoSlQyVXBudTdSandaaktOc0YwV0tuUjZwMzZlNVpjR01mNjVsTTJHc3FHZmNHOVdJWHV0R2VPRjVrRXhwSDcxRk9UMzdCZUdJSDZUNEI3blVzNGVKSUszR3NVNTVkc1dsSE9vVjFudXdhdzBrN0t2VlRYckhlWHlSWDhJMGxuK3U5Ymk0MjBGbkNTMlBOY3FaVWpia1Q3Z0RWVW9tL1I4QW5DRWhXWktnV1ZjR1lQM2k4aGF2cVdvWUNnNEQ1M2hmeThlOEFJWTZIUlAxWU84RnpIaWhDWWswV2pjQ3M4Yk1ydXBIcHJIbk9IMkV1NTBsSW5XMkZBZmhWR0RxTEM0VC9taytIblhiRHBuVFdwNnJ4cjV3VjJ4cUVNM3lPbjJSRThodHRMYXhYYnN3WGdKWE4wNnZFTmRqd1RtYmRJbHlubXN6VE9WbjRNZWg5WVd4RVFDQWZqK3R3OHhUQnJMSVFPRUNtOE55MXZER3AzNWlET2orQ1UvcjdURHQ2VjhiaXViMFNaSEh2Wng4di9OTzdkc1pTdUNuMTIzKzk4bTVkeC9rN1VXTHVTblQ3elZKQit6Q2NXUmUxY3ppaTI0dWs2TGZWUEUzSFBKTUpIbzdJTE9QWVFUbXhyRjBLVldVdXJKc2NVMGo4NWpxVFFORXltZllzOCtoeUhyalpsRFpkdzJvOWJrSTVYSy9rbVVTQWVhc2JvVGY1K2hpZ0JsTDZkL1dhMVlFaFpQSDgxcHlTeTBXU2dWYmRIK21odHV1eXR4RDFTUzNHUFIxWWNlejQySkllWHhjbDVYdlZqRVRjWVE4aWlIS1dRQVkzeW5sSTBWZXNGYW40Yis3Y2NsOWMrTFZqTzVRNEhTeEZkVGcwNlZPQTlFaXIwYjdySm51RTRQN3lwOVBLTG9hOHpPREI4NFpaQmlRdjVBNTBvVGtCdHVyQnk0NTR1OGFHaW0yYm9Dckl2RkhyZmpoMEJ1RmNYbE4zNEhkT0FCVVl4SUZtc1g1OUg0dVJva2FodFl5VWtmc05GYUFqZnlZQnd6Q3BXSGd1R0JqVE1wYU1uWWtHNkRxRWRFcithaC9WREg1TzdhQjczSmxtd2pncWhQNmRudVluL0wwdzcrZ3BwTzRDQkhSczFaSXoxNU5qYmxzZlE5cTF6cmlZVFBwdm5EM1BCTUExWFY5czlmTmRFMTZUSEdTSzJUQ01Va05EcWh2Wm1tVzFpTzI1c0k2RXlMTWM0SmsrQkw1RzhZSWZVWDhTTDZBelVUMU95dmR4TyIsImlhdCI6MTY1NzYzMDg5MSwiZXhwIjoxNjU4ODQwNDkxfQ.tZrgR-ddiPR84i9At68Tabnp9kAzIa-gcYkIhsMlWYg; _ym_d=1657697444; _ym_isad=2; _mlocation=637640; _mlocation_mode=laas; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi5tLmF2aXRvLnJ1JTIyJTJDJTIyZXhwaXJlcyUyMiUzQSUyMlRodSUyQyUyMDEzJTIwSnVsJTIwMjAyMyUyMDEwJTNBMDUlM0EyOCUyMEdNVCUyMiUyQyUyMlNhbWVTaXRlJTIyJTNBJTIyTGF4JTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlN0IlNUMlMjJ2YWx1ZSU1QyUyMiUzQSU1QyUyMjE2NGI4ZjcxODg3N2E0MzcwYjAxNmQ0NmNlMzg1YzVmJTVDJTIyJTJDJTVDJTIyZnBqc0Zvcm1hdCU1QyUyMiUzQXRydWUlN0QlMjIlN0Q=; luri=moskva; v=1657721393; dfp_group=51; isLegalPerson=0; _ym_visorc=b; sx=H4sIAAAAAAACA52SSZLbMAxF76J1L0ASBMi+DQWSckuyPGhWl+8eulLuxFkGB3h4/wPfFYF1kXxIIA4J2RuFQfvI3lOWmqvP72qpPqs5my9lzv1yXrZVQb+0Jw57ew8umgbm6qNK1aciy2wQnXl8VFRGIlP25C0h+cR1MoVsQYSjf5EPc8QNUqZtyJ2xApf52Kdg+0HfYJA/ZAdc9ArZ1ZSSmOSND7UB0OG5A2vUiIIIL/IdTzum9ny6ddP94KZx64o07PsXcuPXv5w9scYnWcRirSOjNSqbZJTJNeVkdMrZcX6RfR/7i9+mxeWhIbZhvO+tnw6d55Sut7c21G/n6FXStdaGasuis88JXXZKABQaeZEHF9Jsd7Pcu5tCOLl4rvvpkt1Ot+VI785KF7JvrxvqHKa+EZARR2hcdxG5vJB9vi1FdOo2685ip97OHXHvOnNlxvZN1qMvyEiWamEJlkl8CpBS0aKAmmJw5P6P/KwhI2Mq0bOTmhR75WLKERVAtmjp590mdb223Wqd/qJpLLdlfed8nRs6BhPPb2QL8HRe5+60mHHfxg6kAVxH6EbBnxpM2a2lBBTJWUvWAJ7KHbikjJpcstrF2sE/D0ePxy+DCtWVJgMAAA==; f=5.9fd3735f16182a28b32428cf8e3c6b5047e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b99364cc9ca0115366433be0669ea77fc074c4a16376f87ccd915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d4047e992ad2cc54b8aa8c772035eab81f5e1e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca746b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba4604438f9f51f7fb331d49c1c93fcdfd7461c4c4543acfc7034638ec26cf48d72d17c7721dca45217ba1938a91a59ce5e68f97af514fc92d30e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa1526da7277fa474771e7cb57bbcb8e0f2da10fb74cac1eabb3ae333f3b35fe91de6c39666ae9b0d73339614c6f29137599c7f25537e9455a; _ga=GA1.2.418341391.1625657273; _dc_gtm_UA-2546784-1=1; tmr_reqNum=202; tmr_detect=0|1657721596018; _ga_9E363E7BES=GS1.1.1657721395.71.1.1657721607.44'
    headers = {
            'authority': 'm.avito.ru',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9',
            'cookie': cookie,
            }
    s.headers.update(headers)
    return s


def writeInLog(message, location):
    f = open('log.txt', mode = 'a')
    f.write(f'Loc: {location}: {message}\n')


def getIDS(filename = 'ids.ini', session = None):
    ids = []
    cicle_stop = True       
    cikle = 0               
    items = []
    url_api_9 = 'https://m.avito.ru/api/11/items'
    params = {
        'categoryId': categoryId,
        'params[536]': 5546,
        'params[554]': 5727,
        'locationId': locationId,
        'withImagesOnly': withImagesOnly,
        'lastStamp': 1657706700,
        'display': 'list',
        'limit': limit_page,
        'query': search,
        'key': key,
    }

    f = open(filename, mode = 'a')             
    while cicle_stop:
        cikle += 1
        params['page'] = cikle
        page = params['page']
        print(f'Страница: {page}')
        res = session.get(url_api_9, params=params)
        try:
            res = res.json()
            g = open('test.json', mode = 'w')
            json.dump(res, g)

        except json.decoder.JSONDecodeError:
            cicle_stop = False
            break
        # print(res)

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
                if not ad_id in ids:
                    ids.append(ad_id)
                    f.write(str(ad_id) + '\n')
    print(f'Всего объявлений: {len(ids)}')
    return filename


def getInfo(id, session):
    url_info = f'https://m.avito.ru/api/18/items/{id}'
    params = {
        'key': key
    }
    info_js = session.get(url_info, params=params).json()
    if not 'error' in info_js:
        f = open('test.json', mode = 'w')
        json.dump(info_js, f)
        return info_js
    else:
        print(info_js)


def ParseInfo(info, title_csv, session):
    try:
        info_parse = []
        for i in range(len(title_csv)):
            info_parse.append('')
        info_parse[0] = info['firebaseParams']['itemID']
        info_parse[1] = info['title']
        info_parse[2]  = info['address']
        info_parse[3]  = info['sharing']['url']
        info_parse[4] = info['price']['value']
        info_parse[5] = info['price']['metric']
        info_parse[6] = info['coords']['lat']
        info_parse[7] = info['coords']['lng']
        
        additionalSeller = info['additionalSeller']['parameters']
        for parameter in additionalSeller:
            title_p = parameter['title']
            if title_p in title_csv:
                info_parse[title_csv.index(title_p)] = parameter['description']
            else:
                print(f'{title_p} не учтен!')
                writeInLog(f'{title_p} не учтен!', 'parseMessage')
                
        parameters = info['parameters']['flat']
        for parameter in parameters:
            title_p = parameter['title']
            if title_p in title_csv:
                info_parse[title_csv.index(title_p)] = parameter['description']
            else:
                print(f'{title_p} не учтен!')
                writeInLog(f'{title_p} не учтен!', 'parseMessage')
                    
        info_parse[28] = info['description']

        images_str = ''

        try:
            for image in info['images']:
                images_str += image['1280x960'] + '; '
        except Exception:
            pass

        info_parse[29] = images_str
         
        info_parse[30] = info['time']

        try:
            info_parse[31] = info['seller']['postfix']
        except Exception:
            pass
        try:
            info_parse[32] = info['seller']['name']
        except Exception:
            pass
        try:
            info_parse[33] = info['seller']['manager']
        except Exception:
            pass

        user_hash = info['seller']['userHash']
        info_parse[34] = f'https://www.avito.ru/user/{user_hash}/profile'
        try:
            params = {
                'categoryId': categoryId,
                'params[536]': 5546,
                'params[554]': 5727,
                'locationId': locationId,
                'withImagesOnly': withImagesOnly,
                'lastStamp': 1657706700,
                'display': 'list',
                'limit': limit_page,
                'query': search,
                'key': key,
                }
            url_get_phone = 'https://m.avito.ru/api/1/items/' + str(info['firebaseParams']['itemID']) + '/phone'
            phone = session.get(url_get_phone, params=params).json()
            info_parse[35] = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1])
        except Exception as e:
            print(e)
            writeInLog(f'Error phone_number', 'parseMessage')
        return info_parse
    
    except Exception as e:
        writeInLog(f'Error {e}', 'parseMessage')
        print(e)
        return None


def SaveInfo(info, file_name = 'data.csv'):
    csvFile = open(file_name, 'a')
    with csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(info)


def main():
    session = raiseSession()
    title_csv = ['ID', 'Название','Адрес','URL',
             'Цена','ЕИ цены','Координаты lat','Координаты lng',
             'Тип здания', 'Класс здания', 'Общая площадь', 
             'Этаж', 'Отделка', 'Залог', 
             'Комиссия, %', 'Категория', 'Парковка', 
             'Тип парковки', 'Отдельный вход',
             'Аренда части площади','Высота потолков, м','Включено в стоимость', 'Несколько этажей',
             'Отопление','Отделка','Вход', 'Количество парковочных мест',
             'Отдельный вход', 'Описание','Изображения', 
             'Дата опубликования', 'Тип продавца','Название компании',
             'Имя продавца','URL продавца', 'Номер телефона']
    
    file_ids = getIDS('ids.ini', session)
    f = open(file_ids, mode = 'r')
    ids = f.readlines()
    SaveInfo(title_csv)
    for i in range(len(ids)):
        info = getInfo(ids[i].strip(), session)
        parse_info = ParseInfo(info=info, title_csv=title_csv)
        if parse_info:
            SaveInfo(parse_info)
            print('Добавлено ' + str(i+1) + ' объявлений')
        else:
            print(f'Ошибка на {i} объявлении, id: {ids[i]}')
            writeInLog(f'Ошибка на {i} объявлении, id: {ids[i]}', 'main')
            # input('Нажмите Enter чтобы продолжить...')
        time.sleep(1)
    f = open('test.json', mode = 'r')
    info = json.load(f)
    ParseInfo(info)


if __name__ == '__main__':
    main()

