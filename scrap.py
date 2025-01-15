import os
import requests
from bs4 import BeautifulSoup

site = 'https://www.jw.org'

response = requests.get(site)

def scrap():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraph = soup.find_all('p')

        content = '\n'.join(p.get_text() for p in paragraph)
        file_path = os.path.join(os.path.expanduser ('~'), 'Documents', 'jw_scrp.txt')
        with open(file_path, 'w', encoding = 'utf-8') as file:
            file.write(content)

        print(f'content gotten successfully')

    else: print(f'unable to get content')
