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
        self.cursor.execute(f'SELECT name, uuid, parents FROM {self.structures_table} WHERE avito_id IS NULL')
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
                    self.parents += "'" + item[1] + "'::uuid,"
                    break
                
        
    def saveItems(self, item, owner_uuid):
        uuid_item = str(uuid.uuid4())
        name = item['Название']
        self.parents = 'ARRAY ['
        structures = self.structures
        try:
            if item['Тип'] == 'container':
                self.parents += "'" + structures['Контейнер'] + "'::uuid,"
            elif item['Тип'] == 'warehouse': 
                self.parents  += "'" + structures['Склад'] + "'::uuid,"
            elif item['Тип'] == 'space':
                self.parents += "'" + structures['Площадка'] + "'::uuid,"
            elif item['Тип'] == 'box':
                self.parents += "'" + structures['Площадка'] + "'::uuid,"
        except Exception:
            pass

        titles = ['Тип здания', 'Классы склада', 'Этаж', 'Отделка', 'Залог','Парковка','Тип парковки','Отдельный вход','Категория', 'Несколько этажей',
            'Отопление','Вход', 'Количество парковочных мест','Описание','Изображения', 'Комиссия, %','Включено в стоимость', 'Аренда части площади']
        
        for title in titles:
            try:
                value = item[title]
                self.InsertIntoParrent(value, title)
            except Exception:
                pass

        try:
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
        except Exception:
            pass
 
        if self.parents != 'ARRAY [':
            self.parents = self.parents[:-1] + ']'
        else:
            self.parents = self.parents + ']'
        
        
        price = int("".join(item["Цена"].split()))
        capacity = float("".join(item["Общая площадь"].split(' ')[0].split()))
        if item['ЕИ цены'] == '₽ в месяц':
            interval = 'month'
        elif item['ЕИ цены'] == '₽ в год':
            interval = 'year'
        elif item['ЕИ цены'] == '₽ в месяц за м²':
            price = price * capacity
            interval = 'month'
        elif item['ЕИ цены'] == '₽ в год за м²':
            price = price * capacity
            interval = 'year'
        lat = item["Координаты lat"]
        lng = item["Координаты lng"]
        coords = f'ARRAY [{lat},{lng}]'
        address = item['Адрес']
        url = item['URL']
        avito_id = item['ID']
        time_load = item['Дата опубликования']
        image_str = ''''{"images": ['''
        for image in item['Изображения']:
            image_str += '"' + item['Изображения'][image] + '",'
        
        if image_str == ''''{"images": [''':
            image_str += "]}'"
        else:
            image_str = image_str[:-1] + "]}'"
        try:
            if item['Аренда части помещения'] == 'Да':
                is_partible = 'true'
            else:
                is_partible = 'false'
        except Exception:
            is_partible = 'false'
        
        url_seller = item['URL продавца']
        name_seller = item['Название компании']
        type_seller = item['Тип продавца']

        try:
            phone_number = item['Номер телефона']
        except Exception:
            phone_number = ''

        query = f'''INSERT INTO public.structures3 (
            id,
            uuid, 
            name, 
            parents, 
            price, 
            coords, 
            address, 
            files, 
            interval, 
            capacity, 
            is_partible, 
            avito_id, 
            url, 
            url_seller, 
            name_seller, 
            type_seller, 
            phone_number,
            owner_uuid
            ) VALUES (
                DEFAULT,
                '{uuid_item}'::uuid,
                '{name}',
                {self.parents},
                {price},
                {coords},
                '{address}',
                {image_str},
                '{interval}',
                {capacity},
                {is_partible},
                {avito_id},
                '{url}',
                '{url_seller}',
                '{name_seller}',
                '{type_seller}',
                '{phone_number}',
                '{owner_uuid}'::uuid
            )
            ON CONFLICT (avito_id) DO UPDATE SET
                name = '{name}', 
                parents = {self.parents}, 
                price = {price}, 
                coords = {coords}, 
                address = '{address}', 
                files = {image_str}, 
                interval = '{interval}', 
                capacity = {capacity}, 
                is_partible = {is_partible},
                url = '{url}',
                phone_number = '{phone_number}'
            ;'''
        
        self.cursor.execute(query)
        self.conn.commit()