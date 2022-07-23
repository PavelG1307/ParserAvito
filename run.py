# https://tgramsearch.com/
# import cloudscraper
import os
from unicodedata import category
import requests
from bs4 import BeautifulSoup
import time

def SavePage(i):
    t = requests.get('https://tgramsearch.com/?page=' + str(i)).text
    # t = request('GET', url).text
    with open(f'./pages/page_{i}.txt', 'w', encoding='utf-8') as f:
        f.write(t)

def SaveLinks(i):
    with open(f'./pages/page_{i}.txt', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

    k = soup.find_all("div", {"class": "tg-channel-wrapper is-list"})
    with open('link.txt', 'a', encoding='utf-8') as f:
        for link in k:
            f.write(link.find('div', {'class': 'tg-channel-link'}).find('a')['href'] + '\n')

def SavePageWithUserName():
    with open('links.txt', 'r', encoding='utf-8') as f:
        links = f.readlines()
    for i in range(len(links)):
        with open(f'page{i}.txt', 'w', encoding='utf-8') as f:
            t = requests.get('https://tgramsearch.com' + links[i][:-1]).text
            f.write(t)
            # pass
            # soup = BeautifulSoup(t, 'lxml')
            # f.write(link.find('div', {'class': 'tg-channel'}).find('div', {'class': 'tg-channel-more'}).find('a')['href'] + '\n')

def SaveUsername():
    with open('href.txt', 'a', encoding='utf-8') as h:
        for i in range(2):
            with open(f'page{i}.txt', 'r', encoding='utf-8') as f:    
                t = f.read()   
                soup = BeautifulSoup(t, 'lxml')
                h.write(soup.find('div', {'class': 'tg-channel'}).find('div', {'class': 'tg-channel-more'}).find('a')['href'] + '\n')

def Parse_Category():
    # tg-categories
    # t = requests.get('https://tgramsearch.com/').text
    with open('cat.txt', 'r', encoding='utf-8') as f:    
        t = f.read()
    soup = BeautifulSoup(t, 'lxml')
    links = soup.find('div', {'class': 'tg-categories-wrapper'}).find_all('a')
    with open('links_category.txt', 'a', encoding='utf-8') as f:    
        for link in links:
            f.write(link['href'] + '\n')

def SaveCategory():
    with open('links_category.txt', 'r', encoding='utf-8') as f:
        categories = f.readlines()
    for cat in categories:
        name = cat[12:-1]
        with open(f'./categories/{name}.txt', 'a', encoding='utf-8') as f: 
            t = requests.get('https://tgramsearch.com' + cat[:-1]).text
            f.write(t)
        time.sleep(5)
        
def SaveLinks_C(name,i):
    with open(f'./categories_dir/{name}/page_{i}.txt', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
    k = soup.find_all("div", {"class": "tg-channel-wrapper is-list"})
    with open(f'./links/{name}.txt', 'a', encoding='utf-8') as j:
        for link in k:
            j.write(link.find('div', {'class': 'tg-channel-link'}).find('a')['href'] + '\n')
            
def SaveLinksFromCat():
    with open('links_category.txt', 'r', encoding='utf-8') as f:
        categories = f.readlines()
    for cat in categories:
        name = cat[12:-1]
        with open(f'./categories/{name}.txt', 'r', encoding='utf-8') as f:
            t = f.read()
        soup = BeautifulSoup(t, 'lxml')
        print(f'page {name}')
        k = soup.find('div', {'class': 'tg-pager-wrapper'})
        if k!=None:
            count_page = int(k.find_all('li')[-1].text)
        else:
            count_page = 1
        print(f'Страниц {count_page}')
        os.mkdir(f'./categories_dir/{name}')
        for i in range(1, count_page + 1, 1):
            link = f'https://tgramsearch.com/categories/{name}?page={i}'
            print(f'Страница {i} из {count_page}')
            t = requests.get(link)
            if t.status_code == 200:
                with open(f'./categories_dir/{name}/page_{i}.txt', 'w', encoding='utf-8') as f:
                    f.write(t.text)
                SaveLinks_C(name,i)
            else:
                break
            time.sleep(1)
                
           
           
def SaveLinkTg():
    with open('links_category_all.txt', 'r', encoding='utf-8') as f:
        categories = f.readlines()
    for cat in categories:
        name = cat[12:-1]
        os.mkdir(f'./join_page/{name}')
        print(f'Категория {name}')
        with open(f'./links/{name}.txt', 'r', encoding='utf-8') as f:
            links = f.readlines()
        c = len(links)
        for i in range(c):
            with open(f'./join_page/{name}/ch_{i}.txt', 'w', encoding='utf-8') as f:
                url = 'https://tgramsearch.com' + links[i][:-1]
                print(f'{i} из {c}')
                t = requests.get(url).text
                f.write(t)
                soup = BeautifulSoup(t, 'lxml')
            with open(f'./link_tg/{name}.txt', 'a', encoding='utf-8') as h:
                try:  
                    h.write(soup.find('div', {'class': 'tg-channel'}).find('div', {'class': 'tg-channel-more'}).find('a')['href'] + '\n')
                except Exception as e:
                    print(e)
            time.sleep(0.2)

# SaveLinksFromCat()
SaveLinkTg()
