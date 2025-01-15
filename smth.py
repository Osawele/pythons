import os
from bs4 import BeautifulSoup
import datetime as datetime
import requests
import re

def web_headers(url):
    print(f'\n [+] HTTP headers for {url}: ')
    response = requests.get(url)
    for key, value in response.headers, items():
        print(f'I found {key}. What it does is {value}')


