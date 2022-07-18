from parser import Parser
from inspector import Inspector
import time
from server import Server
import asyncio

cookie = 'u=2ospkoq5.q3xuox.7fs4jiv87n4; buyer_local_priority_v2=0; _ym_uid=1623759258873598042; sessid=5887d4513ea2d827c428b3d9b8dc93ad.1626951703; __gads=ID=62e4b90be5a4d21a:T=1625657273:S=ALNI_MYDSgTp12uCkXfw-7HFLriUehI8TQ; adrcid=AdN-BkbrhKDUxXDsFGH8omQ; tmr_lvid=b8ddbd48e59db7c09ea3e12b1ba5e547; tmr_lvidTS=1653044851924; _gcl_au=1.1.1656198276.1653987768; buyer_location_id=637640; buyer_laas_location=637640; _gid=GA1.2.1553517392.1657627701; uxs_uid=54224b80-01dc-11ed-abeb-090cbed4b192; __ddg1_=Kr3srU2vCr43yNfdkN36; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISWtQdTBhVzcyRHpGR3NKSHVJWTBqVktoSlQyVXBudTdSandaaktOc0YwV0tuUjZwMzZlNVpjR01mNjVsTTJHc3FHZmNHOVdJWHV0R2VPRjVrRXhwSDcxRk9UMzdCZUdJSDZUNEI3blVzNGVKSUszR3NVNTVkc1dsSE9vVjFudXdhdzBrN0t2VlRYckhlWHlSWDhJMGxuK3U5Ymk0MjBGbkNTMlBOY3FaVWpia1Q3Z0RWVW9tL1I4QW5DRWhXWktnV1ZjR1lQM2k4aGF2cVdvWUNnNEQ1M2hmeThlOEFJWTZIUlAxWU84RnpIaWhDWWswV2pjQ3M4Yk1ydXBIcHJIbk9IMkV1NTBsSW5XMkZBZmhWR0RxTEM0VC9taytIblhiRHBuVFdwNnJ4cjV3VjJ4cUVNM3lPbjJSRThodHRMYXhYYnN3WGdKWE4wNnZFTmRqd1RtYmRJbHlubXN6VE9WbjRNZWg5WVd4RVFDQWZqK3R3OHhUQnJMSVFPRUNtOE55MXZER3AzNWlET2orQ1UvcjdURHQ2VjhiaXViMFNaSEh2Wng4di9OTzdkc1pTdUNuMTIzKzk4bTVkeC9rN1VXTHVTblQ3elZKQit6Q2NXUmUxY3ppaTI0dWs2TGZWUEUzSFBKTUpIbzdJTE9QWVFUbXhyRjBLVldVdXJKc2NVMGo4NWpxVFFORXltZllzOCtoeUhyalpsRFpkdzJvOWJrSTVYSy9rbVVTQWVhc2JvVGY1K2hpZ0JsTDZkL1dhMVlFaFpQSDgxcHlTeTBXU2dWYmRIK21odHV1eXR4RDFTUzNHUFIxWWNlejQySkllWHhjbDVYdlZqRVRjWVE4aWlIS1dRQVkzeW5sSTBWZXNGYW40Yis3Y2NsOWMrTFZqTzVRNEhTeEZkVGcwNlZPQTlFaXIwYjdySm51RTRQN3lwOVBLTG9hOHpPREI4NFpaQmlRdjVBNTBvVGtCdHVyQnk0NTR1OGFHaW0yYm9Dckl2RkhyZmpoMEJ1RmNYbE4zNEhkT0FCVVl4SUZtc1g1OUg0dVJva2FodFl5VWtmc05GYUFqZnlZQnd6Q3BXSGd1R0JqVE1wYU1uWWtHNkRxRWRFcithaC9WREg1TzdhQjczSmxtd2pncWhQNmRudVluL0wwdzcrZ3BwTzRDQkhSczFaSXoxNU5qYmxzZlE5cTF6cmlZVFBwdm5EM1BCTUExWFY5czlmTmRFMTZUSEdTSzJUQ01Va05EcWh2Wm1tVzFpTzI1c0k2RXlMTWM0SmsrQkw1RzhZSWZVWDhTTDZBelVUMU95dmR4TyIsImlhdCI6MTY1NzYzMDg5MSwiZXhwIjoxNjU4ODQwNDkxfQ.tZrgR-ddiPR84i9At68Tabnp9kAzIa-gcYkIhsMlWYg; _ym_d=1657697444; _ym_isad=2; _mlocation=637640; _mlocation_mode=laas; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi5tLmF2aXRvLnJ1JTIyJTJDJTIyZXhwaXJlcyUyMiUzQSUyMlRodSUyQyUyMDEzJTIwSnVsJTIwMjAyMyUyMDEwJTNBMDUlM0EyOCUyMEdNVCUyMiUyQyUyMlNhbWVTaXRlJTIyJTNBJTIyTGF4JTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlN0IlNUMlMjJ2YWx1ZSU1QyUyMiUzQSU1QyUyMjE2NGI4ZjcxODg3N2E0MzcwYjAxNmQ0NmNlMzg1YzVmJTVDJTIyJTJDJTVDJTIyZnBqc0Zvcm1hdCU1QyUyMiUzQXRydWUlN0QlMjIlN0Q=; luri=moskva; v=1657721393; dfp_group=51; isLegalPerson=0; _ym_visorc=b; sx=H4sIAAAAAAACA52SSZLbMAxF76J1L0ASBMi+DQWSckuyPGhWl+8eulLuxFkGB3h4/wPfFYF1kXxIIA4J2RuFQfvI3lOWmqvP72qpPqs5my9lzv1yXrZVQb+0Jw57ew8umgbm6qNK1aciy2wQnXl8VFRGIlP25C0h+cR1MoVsQYSjf5EPc8QNUqZtyJ2xApf52Kdg+0HfYJA/ZAdc9ArZ1ZSSmOSND7UB0OG5A2vUiIIIL/IdTzum9ny6ddP94KZx64o07PsXcuPXv5w9scYnWcRirSOjNSqbZJTJNeVkdMrZcX6RfR/7i9+mxeWhIbZhvO+tnw6d55Sut7c21G/n6FXStdaGasuis88JXXZKABQaeZEHF9Jsd7Pcu5tCOLl4rvvpkt1Ot+VI785KF7JvrxvqHKa+EZARR2hcdxG5vJB9vi1FdOo2685ip97OHXHvOnNlxvZN1qMvyEiWamEJlkl8CpBS0aKAmmJw5P6P/KwhI2Mq0bOTmhR75WLKERVAtmjp590mdb223Wqd/qJpLLdlfed8nRs6BhPPb2QL8HRe5+60mHHfxg6kAVxH6EbBnxpM2a2lBBTJWUvWAJ7KHbikjJpcstrF2sE/D0ePxy+DCtWVJgMAAA==; f=5.9fd3735f16182a28b32428cf8e3c6b5047e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b99364cc9ca0115366433be0669ea77fc074c4a16376f87ccd915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d4047e992ad2cc54b8aa8c772035eab81f5e1e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca746b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba4604438f9f51f7fb331d49c1c93fcdfd7461c4c4543acfc7034638ec26cf48d72d17c7721dca45217ba1938a91a59ce5e68f97af514fc92d30e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa1526da7277fa474771e7cb57bbcb8e0f2da10fb74cac1eabb3ae333f3b35fe91de6c39666ae9b0d73339614c6f29137599c7f25537e9455a; _ga=GA1.2.418341391.1625657273; _dc_gtm_UA-2546784-1=1; tmr_reqNum=202; tmr_detect=0|1657721596018; _ga_9E363E7BES=GS1.1.1657721395.71.1.1657721607.44'
title_csv = ['ID', 'Тип', 'Название','Адрес','URL',
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


def parse_all(parser, inspector, search, owner_uuid, categoryId, locationId):
    try:
        if inspector.add_user_in_parsing(owner_uuid):
            try:
                print(f'location Id {locationId}')
                res = parser.parse(search=search, title_csv = title_csv, owner_uuid=owner_uuid, categoryId=categoryId, locationId=locationId)
                # res = {'st' : 'success'}
                inspector.setResult(res, owner_uuid)
            except Exception as e:
                print(e)
                inspector.add_user_in_error(owner_uuid)
            finally:
                inspector.remove_user_in_parsing(owner_uuid)
    except Exception as e:
        print(e)


def parse(id_hash, owner_uuid, parser, inspector):
    try:
        if inspector.add_user_in_parsing(owner_uuid):
            try:
                res = parser.parse(owner_uuid = owner_uuid,  title_csv = title_csv, categoryId=42, user_id_hash = id_hash, locationId=621540)
                inspector.setResult(res, owner_uuid)
            except Exception as e:
                print(e)
                inspector.add_user_in_error(owner_uuid)
            finally:
                inspector.remove_user_in_parsing(owner_uuid)
    except Exception as e:
        print(e)


def main():
    try:
        parser = Parser(cookie=cookie, log_file='./temp/log.txt', timeout = 2)
        parser.connectDB(dbname='default', user='master', password='6sd1v838', host='194.177.21.255')
        inspector = Inspector()
        serv = Server(port = 8080)
        while(True):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(serv.handl(parser, inspector, parse, parse_all))
    except KeyboardInterrupt:
        serv.server.close()
        print('\nGoodBye')


if __name__ == '__main__':
        main()