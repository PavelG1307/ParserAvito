import json
import time
from session import Session

class Avito():

    def __init__(self, cookie, columns, log_file = 'log.txt', timeout = 1):
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.limit_page = 50
        self.cookie = cookie
        self.log_file = log_file
        self.timeout = timeout
        self.columns = columns
        self.saveInDb = True
        

    def raiseSession(self):
        try:
            s = Session()
            headers = {
                    'Cookie': 'v=1658351465',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'authority': 'm.avito.ru',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'ru-RU,ru;q=0.9',
                    'content-type': 'application/json;charset=utf-8',
                    'referer': 'https://m.avito.ru/items/search?locationId=637640&localPriority=0&geoCoords=55.755814%2C37.617635&presentationType=serp',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
                    'x-laas-timezone': 'Europe/Moscow',
                    'cookie': self.cookie
                    }
            s.headers(headers)
            print(s)
            self.session = s
            return True
        except Exception as e:
            print(e)
            return False


    def writeInLog(self, message, location):
        f = open(self.log_file, mode = 'a')
        f.write(f'Loc: {location}: {message}\n')


    def getIDS(self, filename = './assets/ids/ids.ini'):
        ids = []
        cicle_stop = True       
        cikle = 0               
        items = []
        url_api_9 = 'https://m.avito.ru/api/11/items'

        f = open(filename, mode = 'w')             
        while cicle_stop:
            cikle += 1
            self.params['page'] = cikle
            page = self.params['page']
            print(f'Страница: {page}')
            res = self.session.get(url_api_9, params=self.params)
            try:
                res = res.json()

            except json.decoder.JSONDecodeError:
                cicle_stop = False
                break

            if res['status'] != 'ok':
                    print(res)
                    raise('error in getIds')

            if res['status'] == 'ok':
                items_page = int(len(res['result']['items']))

                if items_page > self.limit_page:
                    items_page = items_page - 1

                for item in res['result']['items']:
                    if item['type'] == 'item':
                        items.append(item)
                    elif item['type'] == 'groupTitle':
                        cicle_stop = False
                        break
                if items_page < self.limit_page:
                    cicle_stop = False
            for item in items:
                if item['type'] == 'item' or item['type'] == 'xlItem':
                    ad_id = str(item['value']['id'])
                    if not ad_id in ids:
                        ids.append(ad_id)
                        f.write(str(ad_id) + '\n')
        print(f'Всего объявлений: {len(ids)}')
        self.fileIds = filename


    def get_ids_from_user(self, id_hash, category_id = 42):
        ids = []
        items = []
        url = 'https://m.avito.ru/api/1/user/profile/items?'
        params = {
            'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
            'limit': 50,
            'sellerId': id_hash,
            'display': 'grid',
            'params[536]': '5546',
            'categoryId': category_id,
        }
        file = './assets/ids/' + id_hash + '.ini'
        f = open(file, mode = 'w')  
        cicle_stop = True
        cikle = 0            
        while cicle_stop:
            cikle += 1
            params['page'] = cikle
            page = params['page']
            print(f'Авито объявления: {page}')
            res = self.session.get(url, params=params)

            try:
                res = res.json()

            except json.decoder.JSONDecodeError:
                cicle_stop = False
                break

            if res['status'] != 'ok':
                    print(res)
                    raise('api error')

            if res['status'] == 'ok':
                items_page = int(len(res['result']['items']))

                if items_page > self.limit_page:
                    items_page = items_page - 1

                for item in res['result']['items']:
                    if item['type'] == 'item':
                        if item['value']['category']['id'] == category_id:
                            items.append(item)
                if items_page < self.limit_page:
                    cicle_stop = False
            for item in items:
                if item['type'] == 'item':
                    ad_id = str(item['value']['id'])
                    if not ad_id in ids:
                        ids.append(ad_id)
                        f.write(str(ad_id) + '\n')

        print(f'Всего объявлений: {len(ids)}')

        self.fileIds = file


    def readIds(self, filename = 'ids.ini'):
        try:
            f = open(filename, mode = 'r')
            ids = f.readlines()
            for i in range(len(ids)):
                ids[i] = ids[i].strip()
            return ids
        except Exception as e:
            print(e)
            return None


    def getInfo(self, id):
        url_info = f'https://m.avito.ru/api/18/items/{id}'
        self.params = {'key': self.key}
        info_js = self.session.get(url_info, params=self.params).json()
        if not 'error' in info_js:
            f = open('./temp/log_req.json', mode = 'w')
            json.dump(info_js, f)
            return info_js
        else:
            print(info_js)
            raise('error')


    def insertToResp(self, data, title):
        if self.saveInDb:
            if title in self.columns:
                self.json_resp[title] = data
            else:
                self.writeInLog(f'{title} не учтен!', 'parseMessage')
        else:
            if title in self.columns:
                self.response[self.columns.index(title)] = data
            else:
                print(f'{title} не учтен!')
                self.writeInLog(f'{title} не учтен!', 'parseMessage')


    def ParseInfo(self, info):
        try:
            if 'контейнер' in info['description'].lower():
                self.insertToResp('container', 'Тип')
                area = float(info['firebaseParams']['area'].split(' ')[0])
                if area <= 15 and area >= 10:
                    self.insertToResp('20', 'Объем контейнера')
                elif area <= 21 and area >= 20:
                    self.insertToResp('20', 'Объем контейнера')
            elif 'площадк' in info['description'].lower():
                self.insertToResp('space', 'Тип')
            elif 'бокс' in info['description'].lower():
                self.insertToResp('box', 'Тип')
            elif 'склад' in info['description'].lower():
                self.insertToResp('warehouse', 'Тип')
            else:
                self.insertToResp('', 'Тип')

            self.insertToResp(info['firebaseParams']['itemID'], 'ID')
            self.insertToResp(info['title'], 'Название')
            self.insertToResp(info['address'], 'Адрес')
            self.insertToResp(info['sharing']['url'], 'URL')
            self.insertToResp(info['price']['value'], 'Цена')
            self.insertToResp(info['price']['metric'], 'ЕИ цены')
            self.insertToResp(info['coords']['lat'], 'Координаты lat')
            self.insertToResp(info['coords']['lng'], 'Координаты lng')
            
            additionalSeller = info['additionalSeller']['parameters']
            for parameter in additionalSeller:
                self.insertToResp(parameter['description'], parameter['title'])
                    
            parameters = info['parameters']['flat']
            for parameter in parameters:
                self.insertToResp(parameter['description'], parameter['title'])
                
            self.insertToResp(info['description'], 'Описание')
            images_str = ''
            image_json = {}

            try:
                for i in range(len(info['images'])):
                    image_json[str(i)] = info['images'][i]['1280x960']
                    images_str += info['images'][i]['1280x960'] + '; '
            except Exception:
                pass
            if self.saveInDb:
                self.insertToResp(image_json, 'Изображения')
            else:
                self.insertToResp(images_str, 'Изображения')
            
            self.insertToResp(info['time'], 'Дата опубликования')

            try:
                self.insertToResp(info['seller']['postfix'], 'Тип продавца')
            except Exception:
                pass
            try:
                self.insertToResp(info['seller']['name'], 'Название компании')
            except Exception:
                pass
            try:
                self.insertToResp(info['seller']['manager'], 'Имя продавца')
            except Exception:
                pass

            user_hash = info['seller']['userHash']
            self.insertToResp(user_hash, 'Hash продавца')
            try: 
                url_get_phone = 'https://m.avito.ru/api/1/items/' + str(info['firebaseParams']['itemID']) + '/phone'
                phone = self.session.get(url_get_phone, params=self.params).json()
                phone_number = self.session.unquote(phone['result']['action']['uri'].split('number=')[1])
                self.insertToResp(phone_number, 'Номер телефона')
            except Exception as e:
                print(e)
                self.writeInLog(f'Error phone_number', 'parseMessage')
            return True
        except Exception as e:
            self.writeInLog(f'Error {e}', 'parseMessage')
            print(e)
            return None


    def parse(self, categoryId, locationId, columns, callback_save, search = 'Склад', user_id_hash = None, save_title=True, only_ids=False, only_info=False, fileIds='./assets/ids/ids.ini', sort = 'priceDesc', withImagesOnly = 'false', priceMin=None, priceMax=None):
        print('Start parsing')
        self.raiseSession()
        self.search = search
        self.categoryId = categoryId
        self.locationId = locationId
        self.ads = []
        self.params = {
            'categoryId': categoryId,
            'params[536]': 5546,
            'locationId': locationId,
            'withImagesOnly': withImagesOnly,
            'lastStamp': 1657706700,
            'display': 'list',
            'limit': self.limit_page,
            'query': search,
            'key': self.key,
            'localPriority': 'true',
            'presentationType': 'serp'
        }

        if priceMin:
            self.params['priceMin': priceMin]
        if priceMax:
            self.params['priceMax': priceMax]
        
        self.columns = columns
        
        if (not only_info):
            if not user_id_hash:
                self.getIDS(fileIds)
            else:
                self.get_ids_from_user(user_id_hash)
        if (only_ids):
            return self.file
        
        ids = self.readIds(filename = self.fileIds)
        for i in range(len(ids)):
            info = self.getInfo(ids[i].strip())
            self.response = []
            for j in range(len(columns)):
                self.response.append('')
            self.json_resp = {}
            parse_info = self.ParseInfo(info=info)

            callback_save(self.json_resp, 'structures3')

            if parse_info:
                self.ads.append(self.json_resp)
                print('Полученно ' + str(i+1) + ' объявлений')
            else:
                print(f'Ошибка на {i} объявлении, id: {ids[i]}')
                self.writeInLog(f'Ошибка на {i} объявлении, id: {ids[i]}', 'main')
                raise 'Error in ParseInfo'
            time.sleep(self.timeout)
        return self.ads

