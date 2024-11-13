import requests
from bs4 import BeautifulSoup

def fetch_page():
    url   = 'https://www.mercadolivre.com.br/apple-iphone-16-pro-1-tb-titnio-preto-distribuidor-autorizado/p/MLB1040287851#polycard_client=search-nordic&wid=MLB5054621110&sid=search&searchVariation=MLB1040287851&position=6&search_layout=stack&type=product&tracking_id=92c2ddf6-f70e-475b-b41e-fe2742459774'
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_='ui-pdp-title').get_text()
    prices: list = soup.findAll('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', ''))
    new_price: int = int(prices[1].get_text().replace('.', ''))
    part_price: int = int(prices[2].get_text().replace('.', ''))

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'part_price': part_price
    }


# Teste da função
if __name__ == '__main__':
    page_content = fetch_page()
    product_info = parse_page(page_content)
    print(product_info)
    #print(page_content)  # Mostra os primeiros 500 caracteres do HTML
