
from modules.avito import Avito
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
            'Имя продавца','URL продавца', 'Номер телефона', 'Hash продавца']


    def connectDB(self, dbname, user, password, host, saveInDb=True):
        try:
            self.db = DBController(dbname=dbname, user=user, password=password, host=host)
            self.saveInDb = saveInDb
            return True
        except Exception as e:
            print(e)
            raise 'Error DB'


    def save_info(self, info, table, file = './assets/data.csv'):
        if self.saveInDb:
            return self.db.saveItems(info, table)
        else:
            csvFile = open(file, 'a')
            with csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(info)
            return None, None


    def parse_user(self, id_hash, inspector, parser_uuid):
        try:
            if inspector.add_user(id_hash, parser_uuid):
                try:
                    parser_avito = Avito(cookie = self.cookie, log_file = './temp/log.txt', timeout = self.timeout, columns = self.columns)
                    res = parser_avito.parse(columns = self.columns, categoryId=42, user_id_hash = id_hash, locationId=621540, callback_save = self.save_info)
                    inspector.setResult(res, parser_uuid)
                    print('Парсинг завершен успешно!')
                except Exception as e:
                    print(e)
                    inspector.add_error(parser_uuid)
                finally:
                    inspector.remove_user(id_hash, parser_uuid)
        except Exception as e:
            print(e)

    
    def parse_region(self, inspector, search, categoryId, locationId, parser_uuid):
        try:
            if inspector.add_uuid(parser_uuid):
                try:
                    parser_avito = Avito(cookie = self.cookie, log_file = './temp/log.txt', timeout = self.timeout, columns = self.columns)
                    res = parser_avito.parse(search=search, columns = self.columns, only_info=True, categoryId=categoryId, locationId=locationId, callback_save = self.save_info)
                    inspector.setResult(res, parser_uuid)
                    print('Синхронизация успешно завершена')
                except Exception as e:
                    print(e)
                    inspector.add_error(parser_uuid)
                finally:
                    inspector.remove_uuid(parser_uuid)
        except Exception as e:
            print(e)





