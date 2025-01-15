import os
import requests
from bs4 import BeautifulSoup

url = 'https://jw.org'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all ('p')
    contents = '\n'.join([p.get_text () for p in paragraphs])
    file_path = os.path.join(os.path.expanduser ("~"), "py-work", "scraped_webpage.txt")
    with open (file_path, 'w', encoding = 'utf-8') as file:
        file.write(contents)
    print (f'content gotten successfully')
else:
    print (f"we couldn't scrape this site")
