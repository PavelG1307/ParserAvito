import requests
import csv
import json
import sys


key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
cookie = 'u=2fkcz6l8.1kgj55.g3xn3vc0t3; _ym_uid=1560267406178859309; buyer_selected_search_radius4=0_general; buyer_selected_search_radius3=0_services; buyer_selected_search_radius2=0_job; buyer_selected_search_radius0=200; buyer_local_priority_v2=0; buyer_index_tooltip=1; auth=1; _gcl_au=1.1.733197779.1652816764; luri=moskva; _ym_d=1657654472; _ym_isad=1; tmr_lvid=5c9c483ac660d500846a4d65251b749d; tmr_lvidTS=1657654489421; _gid=GA1.2.2632564.1657654490; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa858f6718e375efe9248bdd0f4e425aba7085d5b6a45ae867378ba5f931b08c66a72a0378f24244a7a2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabf8e5e9b21a40e18dde87ad3b397f946b4c41e97fe93686adf74ad50eaa2b3372f415355acea9907602c730c0109b9fbb551b50768d5f707e6f9088c33a557ef70e28148569569b7903532f306346f575b9e8022cece544b32ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd74801d2e1440f9b5e4f3de19da9ed218fe23de19da9ed218fe2ddb881eef125a8703b2a42e40573ac3cd81d609ad4115c32bcdb5a5dea4d64cf; ft="4GDrFjTQl5E6tNlykiW1h6a0Clle3t6gkc53Ehj8v2y1ET6ospzoFOy7dn8fB7Q5ynjtpHR3ixYRr9hSVDGMQ0VWF/8Aj1WC46DJue9Xzl/lDZwauU413MCpVeR1MlqodYHJIwCzSLnD12o9lSmk00AXQQWiaYq6ALPFaLyt0iZIBbLKdHLmuFMvXt8GdaDX"; buyer_location_id=637640; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISkRoNkVQZGMzaUhBVjc3QlpVWDhYMG4xS0NKYklyeGVJZkVmSW9SL1FyRDI2dHVKY0dRQzNHODh2WVY5QjNGSWoyOURTOGhvZ2xaM1J5SUNlM3lpOXpuYzZXK0xGcGt3S1o4WmtabTdLT2dJSUFOajFsMzZhQjIyQXRNd1ZPeXZDR1RZRWVsYmtpT1k5TnJPdnE2enpTNzlDakZqTEM2b3JDTE1wNG4xUnl4eDdEQmZEWEpZTDJMZyt0WVZacm1EWjlZeFlxL3BIUEFjSDlBQjhoQmpVUmNKYzF0Qlc4TXhSUTNqUFN1cDBCYmpORUs3YmN1WHlQU0dyenZNdFgvSUk5bHpkN1RZOW9hb2UrVXVGQmhrMlg2ZVdwRUFGK3ZVUjZQYkxJME5zdmxoV3Q3c0p2OUp5eXNPdUZHNE5HVXYvZ1VkRDN2bjh2ZE9aeXNFeHFMNnB2cXVBd28wQXc1dm95cHZQNFcvYXVualNnd0pvWk5GVGZTWHRGY3BUVURXODhDaG9rNVh1U1NBWWU1QnMzWEVDMkYxdUs2K3ZXalRNQnVMTjNCMnFxSXA1N21LLzNYV1ZQcmlVeVBNTS8wN0ZaSXgwUHFwM3Q4bHBFQlh0dGNxdnNPNGhuSGhQRmJVVC94cVZ1OFhXQXYzTHpBZ1hSc3ozL0hKdXFYdGk0OGhzUEVpbkRrMlF0ZDJHNmx2QjJYNzlYRk1WVlc0MmtCWmgvaERQL0JqSjV4aTZTeVdSTEhLS1c5Q2dOcjJQWXpFVE00eW9CbUV6c2VEREtGT3lSQ2NxR25waCtyTGJsa2w0SHlOM2hQMTZWTENxb1g4NXZFUlJ1Tm9QbWYrTHlIcVB2TG9NODEvVVBHdGduU1puakJhWHE2M3FsU0pqcVJ0SjFOc0kwMXVIRzlOb0J4eSt6M3pudXN3MzVacWVFd1BiL2hiYmV5TldlTFlOZ1BxZ0FVdXl3Z2tMSWlMU3pJamVTZEZ4U05weWRBVDArRllWZFU5eWR5Zy9KTjhxaWFSVEtNSjhxY09ZSWhPS2hXdzdzQ3RHYkpZVTVoVHNoZVNidUticElCUVhYb0hDZzVFbGUzRmJLMVBDUUR3YUl5YkdHQmRYdEVWOVFXZHNZa3F3NjZoU0l5ek9iRGs2NVQzd29GelpsVzBHQTUzMWRxd21maW1qSWY2Smdxalg0M1hvMk43c1JPeTMycUxWdEY3QzNGajVmMUVhWkF3WHl6d3VOeUI5Y1I2bkM3aDdsajRMbTB4NU82Y0pqcnNCTFd3WVRFLzAzbjlnT0JvWk1yM3d3WlYyQiIsImlhdCI6MTY1NzY1NzgwNCwiZXhwIjoxNjU4ODY3NDA0fQ.u0ImCa7ThsN2Rdsil-cWSumjBAxXfzbYo1UpCEV03g4; _mlocation=637640; _mlocation_mode=laas; uxs_uid=a2c18040-0221-11ed-87ea-93fc87eb159f; v=1657661110; buyer_laas_location=637640; dfp_group=33; isLegalPerson=0; _ym_visorc=b; redirectMav=1; sx=H4sIAAAAAAAC/5zRSc7jIBBA4buw9oKhKIrcBgqM5wyOjJ1fvnsri0idbS7w6UnvTxhnSUuQllqrIgROrtVGkyHOySkUlz+xiYt4+YeNtb7Gg2/1GikvPN+GyfAzur3eRSOyuCi0zoGSIM9GICJycth69BYBfXYxG5+clcwu+Y/st3bhaeoWBzAOz9DnfOxHLZS2Tkr8X3Zo4WyEIxUxS8qOrMnJ2pZRplYnaayNmD7yQPMa58c9TsNTPVaAZ9+PPQCyvnPcv5s1no3w3ktvICFrDg4So1ZJK6OVU57IfmRKV1XrrGm7HS+oI7BSc6dyOdpoqv6WzbuZ22UfjqzjNNZVch3XIq9rgfVDBjncDjYHpWq3BTua9gHHLhTTdY/wRUrv37EJLUZ2HKxD9jnInClkDKAxBUL6SdbqbES2s6ZlHzNcoRQGWQoUgMo/kdadjejHMbbL3G87FyokQTKvhdefXllznv8CAAD//1V24H67AgAA; _ga=GA1.2.1264586811.1652816766; tmr_detect=0|1657661274813; tmr_reqNum=40; _ga_9E363E7BES=GS1.1.1657657753.4.1.1657661289.5'
search = 'склад'
categoryId = 42
locationId = 637640
sort = 'priceDesc'
withImagesOnly = 'false'
limit_page = 50
s = requests.Session()
# https://m.avito.ru/api/1/rmp/search?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&params[536]=5546&params[110799]=472645&query=%D1%81%D0%BA%D0%BB%D0%B0%D0%B4&categoryId=42&locationId=637640&searchRadius=0
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

if cookie:                                    
    headers['cookie'] = cookie
s.headers.update(headers)                      
s.get('https://m.avito.ru/')                   
url_api_9 = 'https://m.avito.ru/api/11/items'

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
    'key': key,
}


def writeInLog(message, location):
    f = open('log.txt', mode = 'a')
    f.write(f'Loc: {location}: {message}')

def getIDS(filename = 'ids.ini'):
    ids = []
    cicle_stop = True       
    cikle = 0               
    items = []
    f = open(filename, mode = 'a')             
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
        print(res)

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
    print(f'Всего объявлений: {len(ids)}')
    return filename


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

def ParseInfo(info, title_csv):
    try:
        info_parse = []
        for i in range(len(title_csv)):
            info_parse.append('')
            
        info_parse[0] = info['title']
        info_parse[1]  = info['address']
        info_parse[2]  = info['sharing']['url']
        info_parse[3] = info['price']['value']
        info_parse[4] = info['coords']['lat']
        info_parse[5] = info['coords']['lng']
        
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
                    
        info_parse[25] = info['description']
        images_str = ''
        for image in info['images']:
            images_str += image['1280x960'] + '; '
        info_parse[26] = images_str
         
        info_parse[27] = info['time']
        info_parse[28] = info['seller']['postfix']
        info_parse[29] = info['seller']['name']
        info_parse[30] = info['seller']['manager']

        user_hash = info['seller']['userHash']
        info_parse[31] = f'https://www.avito.ru/user/{user_hash}/profile'
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
    print(s.get('https://m.avito.ru/api/18/items/2338321304?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&action=view&context=H4sIAAAAAAAA_0q0MrSqLrYytFKqULIutjI2tFIytCiwLEs2qSyzMK3Iqyw2yEwrSzc2NM03zs3Ir0hOU7KuBQQAAP__5cJxMDUAAAA').text)
    # title_csv = ['Название','Адрес','URL',
    #          'Цена','Координаты lat','Координаты lng',
    #          'Тип здания', 'Класс здания', 'Общая площадь', 
    #          'Этаж', 'Отделка', 'Залог', 
    #          'Комиссия, %', 'Категория', 'Парковка', 
    #          'Тип парковки', 'Отдельный вход','Общая площадь',
    #          'Аренда части площади','Высота потолков, м','Включено в стоимость',
    #          'Отопление','Отделка','Вход',
    #          'Отдельный вход', 'Описание','Изображения', 
    #          'Дата опубликования', 'Тип продавца','Название компании',
    #          'Имя продавца','URL продавца']
    
    # file_ids = getIDS('ids.ino')
    # file_ids = 'ids.ini'
    # f = open(file_ids, mode = 'r')
    # ids = f.readlines()
    # SaveInfo(title_csv)
    # for i in range(len(ids)):
    #     info = getInfo(ids[i].strip())
    #     parse_info = ParseInfo(info, title_csv)
    #     if parse_info:
    #         SaveInfo(parse_info)
    #     else:
    #         print(f'Ошибка на {i} объявлении, id: {ids[i]}')
    #         writeInLog(f'Ошибка на {i} объявлении, id: {ids[i]}', 'main')
    #         input('Нажмите Enter чтобы продолжить...')
    # f = open('test.json', mode = 'r')
    # info = json.load(f)
    # ParseInfo(info)

if __name__ == '__main__':
    main()




#         url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
#         phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
#         if phone['status'] == 'ok': phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1]) # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода)))
#         else: phone_number = phone['result']['message']


