import requests
from bs4 import BeautifulSoup


def get_jumia_data():
    data = requests.get('https://www.jumia.com.ng/laptops/')
    soup = BeautifulSoup(data.text, 'html.parser')
    data_divs = soup.find_all('div', {'class': 'sku -gallery'})
    information = []
    for i in data_divs:
        attributes = {}
        link = i.find('a', {'class': "link"})
        attributes['link'] = link['href']
        name = i.find('span', {'class': "name"})
        attributes['name'] = name.text
        imgs = i.find_all('img')
        img = imgs[1]
        try:
            attributes['image'] = img['data-src']
        except KeyError:
            attributes['image'] = img['src']
        price = i.find('span', {'class': 'price '})
        attributes['price'] = price.text.strip()
        information.append(attributes)
    return information
