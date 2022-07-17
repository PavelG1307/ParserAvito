import requests, pickle
import csv
import json
import time
import sys
from db import DBController

class Parser():

    def __init__(self, cookie, log_file = 'log.txt', timeout = 1):
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.limit_page = 50
        self.cookie = cookie
        self.log_file = log_file
        self.saveInDb = False
        self.timeout = timeout
        

    def connectDB(self, dbname, user, password, host, saveInDb=True):
        try:
            self.db = DBController(dbname=dbname, user=user, password=password, host=host)
            self.saveInDb = saveInDb
            return True
        except Exception as e:
            print(e)
            raise 'Error DB'
            return False


    def changeCookie(self, cookie):
        self.cookie = cookie

    
    def raiseSession(self):
        try:
            s = requests.Session()
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
                    'cookie': self.cookie,
                    }
            s.headers.update(headers)
            self.session = s
            return True
        except Exception as e:
            print(e)
            return False


    def writeInLog(self, message, location):
        f = open(self.log_file, mode = 'a')
        f.write(f'Loc: {location}: {message}\n')


    def getIDS(self, filename = 'ids.ini'):
        ids = []
        cicle_stop = True       
        cikle = 0               
        items = []
        url_api_9 = 'https://m.avito.ru/api/11/items'


        f = open(filename, mode = 'a')             
        while cicle_stop:
            cikle += 1
            self.params['page'] = cikle
            page = self.params['page']
            print(f'Страница: {page}')
            res = self.session.get(url_api_9, params=self.params)
            try:
                res = res.json()
                g = open('test.json', mode = 'w')
                json.dump(res, g)

            except json.decoder.JSONDecodeError:
                cicle_stop = False
                break

            if res['status'] != 'ok':
                    print(res)
                    sys.exit(1)
            if res['status'] == 'ok':
                items_page = int(len(res['result']['items']))

                if items_page > self.limit_page: # проверка на "snippet"
                    items_page = items_page - 1

                for item in res['result']['items']:
                    if item['type'] == 'item':
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
        self.fileIds = filename


    def get_ids_from_user(self, id_hash, category_id = 42):
        ids = []
        items = []
        url = 'https://m.avito.ru/api/1/user/profile/items?'
        params = {
            'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
            'limit': 50,
            'sellerId': id_hash,
            'display': 'grid' 
        }
        file = './assets/ids/' + id_hash + '.ini'
        f = open(file, mode = 'w')  
        cicle_stop = True
        cikle = 0            
        while cicle_stop:
            cikle += 1
            params['page'] = cikle
            page = params['page']
            print(f'Страница: {page}')
            res = self.session.get(url, params=params)
            try:
                res = res.json()
                g = open('./temp/test.json', mode = 'w')
                json.dump(res, g)

            except json.decoder.JSONDecodeError:
                cicle_stop = False
                break

            if res['status'] != 'ok':
                    print(res)
                    sys.exit(1)
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


    def SaveInfo(self, info):
        if self.saveInDb:
            self.db.saveItems(self.json_resp)
        else:
            csvFile = open(self.file, 'a')
            with csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(info)


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
        self.params = {
            'key': self.key
        }
        info_js = self.session.get(url_info, params=self.params).json()
        if not 'error' in info_js:
            f = open('log_req.json', mode = 'w')
            json.dump(info_js, f)
            return info_js
        else:
            print(info_js)


    def insertToResp(self, data, title):
        if self.saveInDb:
            if title in self.title_csv:
                self.json_resp[title] = data
            else:
                print(f'{title} не учтен!')
                self.writeInLog(f'{title} не учтен!', 'parseMessage')
        else:
            if title in self.title_csv:
                self.response[self.title_csv.index(title)] = data
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
            self.insertToResp(f'https://www.avito.ru/user/{user_hash}/profile', 'URL продавца')
            try: 
                url_get_phone = 'https://m.avito.ru/api/1/items/' + str(info['firebaseParams']['itemID']) + '/phone'
                phone = self.session.get(url_get_phone, params=self.params).json()
                phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1])
                self.insertToResp(phone_number, 'Номер телефона')
            except Exception as e:
                print(e)
                self.writeInLog(f'Error phone_number', 'parseMessage')
            return True
        except Exception as e:
            self.writeInLog(f'Error {e}', 'parseMessage')
            print(e)
            return None


    def parse(self, search, categoryId, locationId, title_csv, user_id_hash = None, save_title=True, only_ids=False, only_info=False, fileIds='ids.ini', file = 'data.csv', sort = 'priceDesc', withImagesOnly = 'false', priceMin=None,priceMax=None):
        self.raiseSession()
        self.search = search
        self.categoryId = categoryId
        self.locationId = locationId
        self.params = {
            'categoryId': categoryId,
            'params[536]': 5546,
            'params[554]': 5727,
            'locationId': locationId,
            'withImagesOnly': withImagesOnly,
            'lastStamp': 1657706700,
            'display': 'list',
            'limit': self.limit_page,
            'query': search,
            'key': self.key,
        }

        if priceMin:
            self.params['priceMin': priceMin]
        if priceMax:
            self.params['priceMax': priceMax]
        
        self.title_csv = title_csv
        self.file = file
        if (not only_info):
            if not user_id_hash:
                self.getIDS(fileIds)
            else:
                self.get_ids_from_user(user_id_hash)
        if (only_ids):
            return self.file
        if (save_title and not self.saveInDb):
            self.SaveInfo(info = title_csv)
        ids = self.readIds(filename = self.fileIds)
        
        for i in range(len(ids)):
            info = self.getInfo(ids[i].strip())
            self.response = []
            for j in range(len(title_csv)):
                self.response.append('')
            self.json_resp = {}
            parse_info = self.ParseInfo(info=info)
            if parse_info:
                self.SaveInfo(self.response)
                print('Добавлено ' + str(i+1) + ' объявлений')
            else:
                print(f'Ошибка на {i} объявлении, id: {ids[i]}')
                self.writeInLog(f'Ошибка на {i} объявлении, id: {ids[i]}', 'main')
            time.sleep(self.timeout)