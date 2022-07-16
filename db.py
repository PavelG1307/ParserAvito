import psycopg2
import uuid

class DBController:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
        self.cursor = self.conn.cursor()
        self.structures_table = 'structures3'
        self.getStructures()

    def executeAll(self, tablename):
        self.cursor.execute(f'SELECT * FROM {tablename}')
        return self.cursor.fetchall()

    def getStructures(self):
        self.cursor.execute(f'SELECT name, uuid, parents FROM {self.structures_table} ')
        self.structures = {}
        self.uuid_i = {}
        self.resp = self.cursor.fetchall()
        for i in range(len(self.resp)):
            self.structures[self.resp[i][0]] = self.resp[i][1]
            self.uuid_i[self.resp[i][1]] = self.resp[i][0]
        
    def close(self):
        self.cursor.close()
        self.onn.close()

    def InsertIntoParrent(self, value, parent):
        for item in self.resp:
            if item[0] == value:
                name_parent = self.uuid_i[item[2][1:-1].split(',')[0]]
                if name_parent == parent:
                    self.parents.append(item[1])
                    break
                
        
    def saveItems(self, item):
        structures = self.structures
        self.parents = []
        try:
            if item['Тип'] == 'container':
                self.parents.append(structures['Контейнер'])
            elif item['Тип'] == 'warehouse': 
                self.parents.append(structures['Склад'])
            elif item['Тип'] == 'space':
                self.parents.append(structures['Площадка'])
            elif item['Тип'] == 'box':
                self.parents.append(structures['Площадка'])
        except Exception:
            pass

        avito_id = item['ID']
        name = item['Название']
        address = item['Адрес']
        url = item['URL']
        price = item["Цена"]
        capacity = item["Общая площадь"].split(' ')[0]
        if item['ЕИ цены'] == '₽ в месяц':
            interval = 'month'
        elif item['ЕИ цены'] == '₽ в год':
            interval = 'years'
        elif item['ЕИ цены'] == '₽ в месяц за м²':
            price = price * capacity
            interval = 'month'
        elif item['ЕИ цены'] == '₽ в год за м²':
            price = price * capacity
            interval = 'years'
            
        
        # url_seller = item['URL продавца']
        # name_seller = item['Название компании']
        # type_seller = item['Тип продавца']
        # time_load = item['Дата опубликования']
        
            # 'Аренда части площади'
            # 'Номер телефона'
            # 'Имя продавца'
            
        titles = ['Тип здания', 'Классы склада', 'Этаж', 'Отделка', 'Залог','Парковка','Тип парковки','Отдельный вход','Категория', 'Несколько этажей',
            'Отопление','Вход', 'Количество парковочных мест','Описание','Изображения', 'Комиссия, %','Включено в стоимость', 'Аренда части площади']
        
        for title in titles:
            try:
                value = item[title]
                self.InsertIntoParrent(value, title)
            except Exception:
                pass
        if item['Высота потолков, м']:
            h = float(item['Высота потолков, м'])
            if h <= 1:
                self.InsertIntoParrent('1', 'Высота потолка, м')
            elif h <= 2:
                self.InsertIntoParrent('2', 'Высота потолка, м')
            elif h <= 3:
                self.InsertIntoParrent('3', 'Высота потолка, м')
            elif h <= 4:
                self.InsertIntoParrent('4', 'Высота потолка, м')
            elif h <= 5:
                self.InsertIntoParrent('5', 'Высота потолка, м')
            elif h > 5:
                self.InsertIntoParrent('Более 5 метров', 'Высота потолка, м')
        # value = item[titles[1]]
        # self.InsertIntoParrent(value, titles[1])
        # coords = {item["Координаты lat"], item["Координаты lng"]}
        print(self.parents)
        # print(self.executeAll('structures3'))
        pass