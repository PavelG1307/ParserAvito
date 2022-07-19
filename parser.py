
from avito import Avito
from db import DBController
import csv

class Parser():

    def __init__(self, cookie, timeout=5,  saveInDb=True):
        self.cookie = cookie
        self.saveInDb = saveInDb
        self.timeout = timeout
        self.columns = ['ID', 'Тип', 'Название','Адрес','URL',
            'Цена','ЕИ цены','Координаты lat','Координаты lng',
            'Тип здания', 'Класс здания', 'Общая площадь', 'Объем контейнера',
            'Этаж', 'Отделка', 'Залог', 
            'Комиссия, %', 'Категория', 'Парковка', 
            'Тип парковки', 'Отдельный вход',
            'Аренда части площади','Высота потолков, м','Включено в стоимость', 'Несколько этажей',
            'Отопление','Вход', 'Количество парковочных мест',
            'Отдельный вход', 'Описание','Изображения', 
            'Дата опубликования', 'Тип продавца','Аренда части площади','Название компании',
            'Имя продавца','URL продавца', 'Номер телефона']


    def connectDB(self, dbname, user, password, host, saveInDb=True):
        try:
            self.db = DBController(dbname=dbname, user=user, password=password, host=host)
            self.saveInDb = saveInDb
            return True
        except Exception as e:
            print(e)
            raise 'Error DB'


    def save_info(self, info, owner_uuid, table, file = './assets/data.csv'):
        if self.saveInDb:
            return self.db.saveItems(info, owner_uuid, table)
        else:
            csvFile = open(file, 'a')
            with csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(info)
            return None, None


    def parse_user(self, id_hash, owner_uuid, inspector, parser_uuid):
        try:
            if inspector.add_user(id_hash, parser_uuid):
                try:
                    parser_avito = Avito(cookie = self.cookie, log_file = './temp/log.txt', timeout = self.timeout, columns = self.columns)
                    res = parser_avito.parse(columns = self.columns, categoryId=42, user_id_hash = id_hash, locationId=621540)
                    response = {}
                    for i in range(len(res)):
                        uuid, data = self.save_info(res[i], owner_uuid, 'structures3')
                        response[uuid] = data
                        print('Добавленно ' + str(i+1) + ' объявлений')
                    inspector.setResult(response, parser_uuid)
                except Exception as e:
                    print(e)
                    inspector.add_error(parser_uuid)
                finally:
                    inspector.remove_user(id_hash, parser_uuid)
        except Exception as e:
            print(e)

    
    def parse_region(self, inspector, search, owner_uuid, categoryId, locationId, parser_uuid):
        try:
            if inspector.add_uuid(parser_uuid):
                try:
                    parser_avito = Avito(cookie = self.cookie, log_file = './temp/log.txt', timeout = self.timeout, columns = self.columns)
                    res = parser_avito.parse(search=search, columns = self.columns, categoryId=categoryId, locationId=locationId)
                    response = {}
                    for i in range(len(res)):
                        uuid, data = self.save_info(res[i], owner_uuid, 'structures3')
                        response[uuid] = data
                        print('Полученно ' + str(i+1) + ' объявлений')
                    inspector.setResult(response, parser_uuid)
                except Exception as e:
                    print(e)
                    inspector.add_error(parser_uuid)
                finally:
                    inspector.remove_uuid(parser_uuid)
        except Exception as e:
            print(e)





