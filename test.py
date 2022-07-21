import pickle
import time
import requests
import urllib.request;

proxy = {'https': 'http://julu13-cc-ANY:Ghjugfr123!@gw.ntnt.io:5959'}


    


s = requests.Session()
cookie ='adrcid=AiF3G-MtGYHsHP3-osfjtSA; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISXk1eGhiaFlNK3ExcGpGWXBqYTNxZVFWU3R1aWtPYlJEa1J5VjcvWkEyMU00WWJHeEE0dzRFWFBSYWRKM2ozNVFqdkxyMXFNQ2NDNng3eGxXUWRJMlFYNnVCWjRQZW16Nkp4WWlWb1NlWUZFU2xvMTMxdFNucW9aQUZodGZFZGI3cDFMWDdDNHBlSXVvZlozeTI5aTZoSFhNcGo4N29qUHIvWHJnR3o2NUlqWHY2WWlWdlhHd0l1U0hkSThZbTkwUkZsZFRIMDZkOHR1SU9DbXhCYnlMODQ3aWRveWdRNDVMZTcwZDBleUwxL2JuNzdTMjlnWGJoRUdVNEx4TFRCVEMwdHNSWko2ZnpwTFdPRklWbEo4RjdTWE1MQmt3M216K0lha2o2WHovVFJPdWRZaVJtTUE4c3djZDFFMndXLzRqYit1eDFOcERyNEt4RXRlTDM1djVoYjIxSDgyZ1kxNUFnU0ovQ056NXU3bFhMeW1xTU93T1pRMlFmRFB2anVyL3ljcUFZbTFteks2VFVaTWFGaHk4c0YxOEpBWmhoVlorVDQ5cWtzbVY4QlFBZlYwUU1ON0pUZW9PQUlSNGR0ODdhMlljZWM2R3NLeXdDMWhjWTQ4V09QOWxRZ0UvblltZXpGVnFrQUdRSjlBTlBwYXVtZkxYNFhSUTB2TmkzZmdrSCtUdXBsYWpMZ1A5cC9nR2ZCdlZWVWtlNXlTMGZ6TFRuUGZ2eWVZcE9nbmpNenJVeGZ0NkNQSG9KV2Y3K0Q2MkNaY2ZnOUNCVjZUQmVkdlpPVC95STg2Z0VRNlEzcXhoWE4xNmpoUHBVNldaQkxmays1RGxjV1lac3JSSWUrSEdWL09hS1pTR0NnSzNpdHQva0p6dGhIemJPQng0U3NQL2lBSktzNGt0Z25LZUxmbUEvdE9MeHVUbTJ2UHlidzZKdUovM0lSWkxYaWVoNVlwK045ZlJCcER1c2pFV0tnaVRLbXgwL1N3OUIvSzV5SzkxVmpXWTNvdzN5eXJnRWRhMCtNMWVCL3VYWEdILzdZUG8vUTBEVjFmSmJtejQ0MWF4akhzSzVhVFRJbXZxZWp4a2l1S1ZnQWRFQ09ZWFNwQWdzQ2ZvM01CUkE2RmxIYmNrczB6Q29aQkIrcW05SFdSRGRQS1YwVHNIcUp4c0pjaXBtekp4NU54UkV5K3dNSnBQU0RjRHRURTVrY3IrK3J5RjJMMkNRQ3ZWa1ZSMGhQS0ZnZ0plRXAwZ2Q0a0VmRzhmWjF6czVuczdJby8zRHlyYjZCVjFVdndqTTIvOVpQY2I1SU1NLyIsImlhdCI6MTY1ODM1MjQ1NCwiZXhwIjoxNjU5NTYyMDU0fQ.RM1eSAG6QoV4icElVDDfAEOcDnZZlxe1Q62ItF49iPk; buyer_laas_location=652430; luri=ryazan; buyer_location_id=652430; _ym_uid=165835248128205446; _ym_d=1658352481; u=2teb466n.ahj8h7.bbvyloc1zco0; _gid=GA1.2.1366855477.1658352503; tmr_lvid=09e744f3b93f2ff73cab60787050dd21; tmr_lvidTS=1658352503506; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa858f6718e375efe9248bdd0f4e425aba7085d5b6a45ae867378ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac71e7cb57bbcb8e0ff0c77052689da50ddc5322845a0cba1aba0ac8037e2b74f9f0c77052689da50d2da10fb74cac1eabf0c77052689da50d0df103df0c26013a0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adf74ad50eaa2b3372f415355acea9907602c730c0109b9fbb551b50768d5f707e6f9088c33a557ef70e28148569569b7903532f306346f575b9e8022cece544b32ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748b0d143e001cdaeee3de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03; ft="2452n+tlcxvjANckkXl0iAT6huulSwENZC8B2uH788aZxivlg8cYmQshTaLhpXplFHSSzaYY13WVLMkfarVKrbaMXO7mUoQbUkufFmw2P2e+gjGx5sIjwFU1HBNZwDgNkw0X4NORug/G6F+wPXBABhJ2M2cjs0Oj/vqqAqdEnMYXmwKxgoMnj5i95vs5gJ0J"; _gcl_au=1.1.365228172.1658352755; v=1658429782; sx=H4sIAAAAAAAC/0TMXW6DMAwA4Lv4mYf8EMfmNomdCA00wmDZWsTd+1T1At8FiIiiESsjBxyRS8zFs8ZgRKIyTBd0mGCX33DaxZT/w/W5tmf8GUvpp84+zX8bDFBgshgoWLTk7wFqJsoxKypb40xCVR+IUtWkJDm+5bz6dWnNrO3btN3pISltzciDe/469SOPnq2j+34FAAD//yUD6wW1AAAA; dfp_group=13; _ym_isad=1; _ym_visorc=b; _dc_gtm_UA-2546784-1=1; _mlocation=652430; _mlocation_mode=laas; tmr_reqNum=75; _ga=GA1.1.608462673.1658352503; tmr_detect=0|1658429804297; _ga_9E363E7BES=GS1.1.1658429790.2.1.1658429806.44'
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
                    'cookie': cookie,
                    }

# headers = {
#     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
#     'Cookie': 'dfp_group=39; u=2tebp628.ahj8h7.suli4y791vg; v=1658431472; _mlocation=652430',
# }

def getCookies(cookie_jar, domain):
    cookie_dict = cookie_jar.get_dict(domain=domain)
    found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
    return ';'.join(found)

for i in range(2):
    resp = s.get('https://m.avito.ru/')
    print(resp)
    print(resp.headers)
    print(resp.cookies)
    print(getCookies(resp.cookies, ".avito.ru"))
    time.sleep(3)



