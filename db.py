import psycopg2

class DBController:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
        self.cursor = self.conn.cursor()
        self.structures_table = 'structures3'
        print(self.getStructures())

    def executeAll(self, tablename):
        self.cursor.execute(f'SELECT * FROM {tablename}')
        return self.cursor.fetchall()

    def getStructures(self):
        self.cursor.execute(f'SELECT name, uuid, parents FROM {self.structures_table} ')
        return self.cursor.fetchall()
        
    def close(self):
        self.cursor.close()
        self.onn.close()

    def saveItems(self, item):
        avito_id = item['ID']
        name = item['Название']
        address = item['Адрес']
        url = item['URL']
        price = item["Цена"]
        capacity = int(item["Общая площадь"].split(' ')[1])
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
        coords = {item["Координаты lat"], item["Координаты lng"]}
        # print(self.executeAll('structures3'))
        pass