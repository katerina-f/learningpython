
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool
import requests
from datetime import datetime

def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all'
    all_links = get_links(get_html(url))

    with Pool(40) as p:
        p.map(make_all, all_links)

    time = datetime.now() - start
    print(str(time))

def make_all(url):
    html = get_html(url)
    write_csv(get_page_data(html))

def get_html(url):
    response = requests.get(url)
    return response.text

def get_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []

    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1').text.strip()
    except:
        pass

    try:
        price = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text.strip()
    except:
        pass

    data = {'name': name, 'price': price}

    print(data['name'], 'parsed')
    return data

def write_csv(data):
    with open('coinmarket.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

if __name__ == "__main__":
    main()
