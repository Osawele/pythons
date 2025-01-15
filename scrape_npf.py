import os
from bs4 import BeautifulSoup
import requests


input_url = input("Type in a WEBSITE. Press the 'Enter' key when you're done.\n (Please include 'https://' or not ;-D ): ")
uri = 'https://'

if uri in input_url:
    response = requests.get(input_url)
else:
    url = uri + input_url
    response = requests.get(url)

def resp():
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            homepage_backlinks = soup.find_all('a')
            file_content = '\n'.join([a.get_text() for a in homepage_backlinks])    #Sir, please I don't fully understand this line.
            file_path = os.path.join(os.path.expanduser('~'), 'py-work', input_url + '.txt')
            with open(file_path, 'w', encoding = 'utf-8') as file:
                file.write(file_content)
            print('Scrape Successful!')

        else:
            print("Check the website and try again. We couldn't scrape this website.")

    except:
        print('Something went wrong. Check the code and try again')


resp()



