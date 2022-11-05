import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

# Métodos para busca
# Seletores
# find ou find_all

# print(html.select_one('.s-post-summary'))


for pergunta in html.select('.s-post-summary'):
    texto_pergunta = pergunta.a['href']
    print(f'https://pt.stackoverflow.com{texto_pergunta}')

