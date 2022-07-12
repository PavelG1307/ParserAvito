import requests
import csv
import json
import sys

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
cookie = '_ga_9E363E7BES=GS1.1.1657659578.1.1.1657659740.60; v=1657659576; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi5tLmF2aXRvLnJ1JTIyJTJDJTIyZXhwaXJlcyUyMiUzQSUyMldlZCUyQyUyMDEyJTIwSnVsJTIwMjAyMyUyMDIxJTNBMDElM0EwNiUyMEdNVCUyMiUyQyUyMlNhbWVTaXRlJTIyJTNBJTIyTGF4JTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlN0IlNUMlMjJ2YWx1ZSU1QyUyMiUzQSU1QyUyMmQ1ZjMzMDljNzgwZjQ3ZDUxMzU2ZDg3YjhiYjJkZGMxJTVDJTIyJTJDJTVDJTIyZnBqc0Zvcm1hdCU1QyUyMiUzQXRydWUlN0QlMjIlN0Q=; dfp_group=47; _mlocation=637640; _mlocation_mode=laas; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISlY4RUZWMTljb3lDSS82RnpVNGU4WU5NN0tKeS9OekhKTk9KaUNUcXN6Ny9HblJPMVlnY3Fxcml1RzZuZzBLZ1Q3Z2lGNUZjRFQ1aFlraUhPM004b1hCWVRpemIvSzcySjIrTGRLREY1QWJjdHVVYjNHNWdSNENhemZRSUI3aWI5Ylo5S0R2VngxaDc3b3puS3NRMXZjbklFV2JjQng1ZlF6TzJhNngyb2g3cTF3emRrYTlVNm9sRGh2bjJDWkcvTjJ6VHdzV0ZtVGtPSUpFTTJwa1ZpVkZ4TzBMUlFPMVdPN045a1ZPdTgvNUFDU29QVXdDOC80N1VDMlNoTVJUcEl4T0ZQcVpPNnJ2amRyU0h3d2RjMTZZN0JxSGEwQm10OG9FS2c4NHQwL1ljelRBMWtteUplcjNXbTdJNTNBSTdGMzFzWWJqNENjSy9JK3BIbUFJbFFCYzBqdkw1QXRLM0F2UnJpRzRGa3lWUDNMSFRobTVZQ3ZUVGVCc09hMk5CcExEZStqQS9DaHlZOGlHS3RVZjhuOUlxdlRqZFJrQ1ZRNE5GSGsxYkc3Z3FYRXhJTXB1T0hLMXJ0NlJQUCtpZnBWN0RjZllHNEJRWGpQNmEvSHpaR3oyVkwwdUZValovM2w4RURGeHpMZlM3UnpnRU1Nb3RIM0Y3Z3pkalRFcGorNXBqd3FEQWF1S016T1U2RUhmb1NDWGd5VjFocXJZRmd1bDJ3WEhVV1RwaEJsSHRwNkFITWJhZXhZTW5aWWtjYjFpbHA3b0NKbGUwaFZtMWUxUzFWKzIzWERlRU1VZHZaUm5SMTM5TmtrZzU3S1YwdEYwdVVxWGVDNGpaZHhXN1FnWVdxUmhEK0QyV1hSUDJNSUw1eXpxcllmSzVUNXVUUHNBaGFTM1pXamlpd2REdmVuejloMzdQWmI2Vkw1dElSeWhFN1JDMkppcXlJczZLMStsVUVwRlNDVFV2N3IzdHMwYk9oMUFWUndaTHYxNnVMVmMzMVpOL2pKd0Y2M29SV2xCOWZwRjZ5Y2ZHNDhMbCttSmdjTUJySEtWRXFnWlowTExIaFgzeitBek9na1Z5Y1pCQW0zM1lxRFUvSm8wOHRCN2lLSVl1cTE1NVVoOUNuenZJeTZEZENxTmxiYmE1TXZGT2g3WlhOWnp3PT0iLCJpYXQiOjE2NTc2NTk2MDEsImV4cCI6MTY1ODg2OTIwMX0.JnwxxWb0pR_hMDBCWcRUJp9V9EY8fXLBtUX4KsYhXJU; tmr_reqNum=7; tmr_detect=0%7C1657659644403; _ga=GA1.1.114331317.1657659578; _gid=GA1.2.1489576562.1657659579; tmr_lvid=eeef370a7b3370f0eb8e36fa0b487125; tmr_lvidTS=1657659578839; f=5.e1ae7f0eb55e91e9c738a39f956d9a5c16d443061c57ac4216d443061c57ac4216d443061c57ac4216d443061c57ac42cec4d980e289734fcec4d980e289734fcec4d980e289734f96a296658223dafb96a296658223dafb381ebd593ffbb4c30df103df0c26013a8b1472fe2f9ba6b90df103df0c26013a268a7bf63aa148d2ea5c223d6b439c9d5f5fef956c8c12f948717a87126911fa1cbff88f85149ecf4a5611862bd91ca7e2415097439d4047143114829cf33ca787829363e2d856a2d50b96489ab264edc772035eab81f5e187829363e2d856a2f88859c11ff008953de19da9ed218fe23de19da9ed218fe2c772035eab81f5e13de19da9ed218fe2143114829cf33ca7bed76bde8afb15d28e3a80a29e104a6c2c61f4550df136d8b52ccfba5f649ac597bc64b9d3449ed41da9f488c469f075bcaaee87a280b624d6eebeac28b9a9f02d57da0d3d3274b10616349da3da33c3f009e5192741225146b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac7c629922cb33e217f1f94a407205ae132da10fb74cac1eab2da10fb74cac1eab15fe31d52e5b1f9a711bc502486cd628; ft="VfLqAIggFQ9o/I6cm9jBoogxlhfMy+sJAk0HaglTzn8iH05//tOB46I2U3tfXTf398CNJrVT5JwvUcvgQU95TaT3PZMUlJ9AfH7tim9I6v93wEW4yC72FwnqtL7hyf+EZS8TBMlyi+QRUnsvAfab72iREtkZNt18pgw/AcS3pyjX34a26Kn3syV8BP6UIHHL"; adrcid=A6-8WejCF6isSNpbB8jvpSA; adrdel=1; _gcl_au=1.1.601596732.1657659578; u=2te6ck1c.1cwcd17.7b32ehurnuk0'
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
print(s.get('https://m.avito.ru/').text)                   
url_api_9 = 'https://m.avito.ru/api/1/rmp/'

params = {
    'categoryId': categoryId,
    'params[536]': 5546,
    'params[110799]': 472645,
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
    url_info = f'https://m.avito.ru/api/1/rmp/show/{id}'
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
    res = s.get('https://m.avito.ru/api/1/rmp/show/2338321304?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir')
    print(res)
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


