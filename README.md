# DataSync
#### Install:
Для работы модуля нужен Python3 и следующие библиотеки к нему:
- requests
- uuid
- asyncio
- urllib

`pip3 install  --upgrade --force-reinstall requests uuid asyncio urllib3 psycopg2.binary`

------------



#### Run
Для запуска выполните команду:
`python3 main.py`

------------



#### Usage
<<<<<<< HEAD
##### Синхронизация объявлений пользователя:
Для синхронизации объявлений конретного пользователя необходимо отправить следующий GET запрос:
`/api/avito/user?user=ID_HASH_USER&owner_uuid=OWNER_UUID`
=======
##### Парсинг объявлений пользователя
Для парсинга объявлений конретного пользователя необходимо отправить следующий GET запрос:
`IP_ADDRESS/api/parse/user?user=ID_HASH_USER&owner_uuid=OWNER_UUID`
>>>>>>> 1074b5d (edit: incapsulated avito)

ID_HASH_USER можно получить из ссылки на страницу профиля авито, например:
`https://www.avito.ru/user/c6c5eaa1421b9335f9c2696ae9d40a24/profile?id=2435393350&src=item&page_from=from_item_card&iid=2435393350`

`ID_HASH_USER = c6c5eaa1421b9335f9c2696ae9d40a24`

OWNER_UUID необходим для базы данных

<<<<<<< HEAD
##### Синхронизация объявлений региона:
=======
##### Парсинг объявлений региона
>>>>>>> 1074b5d (edit: incapsulated avito)

`/api/avito/region?owner_uuid=OWNER_UUID&search=SEARCH&locationId=LOC_ID&catedotyId=CAT_ID`

OWNER_UUID необходим для базы данных
SEARCH – поисковой запрос
LOC_ID – ID региона поиска, список ID можно посмотреть по следующей ссылке: `https://rest-app.net/api/city`(необязательное поле, по умолчание выбран регион –  вся Россия)
CAT_ID – ID категорий (необязательное поле, по умолчание выбрана категория – «Коммерческая недвижимость»)

##### Пример ответа
`{'status': 'ok', 'parser_uuid': '88de4051-016b-45bc-8483-afa957a90f46'
}`
где status принимает значения: ok и bad request,
parser_uuid – uuid парсера, необходим для дальнейщего контроля за парсингом

##### Проверка состояния синхронизации:
Для проверки состояния, необходимо выполнить следующий GET запрос:
`/api/avito/check?uuid=PARSER_UUID`
где PARSER_UUID – uuid, который был присвоен и передан в ответ на запрос, в начале синхронизации

<<<<<<< HEAD
##### Примеры ответов:
1. Синхронизация в процессе выполнения:
=======
##### Примеры ответа
1. Парсинг в процессе выполнения:
<<<<<<< HEAD
>>>>>>> 1074b5d (edit: incapsulated avito)
```json
{'status': 'In progress'}
```
2. Синхронизация завершена:
```json
=======
```
{'status': 'In progress'}
```
2. Парсинг завершен:
```
>>>>>>> 41aba40 (edit README)
{'status': 'Done',
 'result': {
        	'62ab92d6-641d-4a41-bbb8-0822b70625f1': {
        			'name': 'Офисное помещение, 58.7 м²', 
        			'avito_id': '1798932250'
        	},
        	'10f354a4-cf90-42a1-a753-90a70105e2c7': {
        			'name': 'Офис, 50.6 м²',
        			'avito_id': '2470727707'
        	},'50e08e40-6fb1-43ae-8699-0c286855ad1c': {
        			'name': 'Офис, 16.4 м²',
        			'avito_id': '2150281413'
        	},
        	'70adb8c2-6b81-4a0a-8094-bb3320d2bbaa': {
        		'name': 'Склад, 149 м²',
        		'avito_id': '2469924232'
        	}
        }
}
```
3. Ошибка:
```
{'status': 'Bad request'}
```

#### P.S.
Если модуль не работает, необходимо заменить cookies в main.py, 6 строка

