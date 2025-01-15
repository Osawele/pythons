import requests
import os
from bs4 import BeautifulSoup
import datetime as datetime
import re

def get_headers(url):
    print(f'\n [+] HTTP Headers for{url}:')
    response = requests.get(url)
    for key, value in response.headers, items():
        print(f"{key} : {value}")

print ("\n [+] security header-analysis: ")

security_headers = {
    "content-security-policy" : "prevents a wide of attacks",
    "strict-transport-security" : "force browsers to use https",
    "x-content-type-options" : "prevents mime-sniffing",
    "x-frame-options" : "prevents clickjacking",
    "x-xss-protection" : "prevents protection against cross site scripting attack xss"
}

for header, purpose in security_headers.items():
    if header not in response.header:
        print(f"[-]{header} is missing ({purpose})")
    else:
        print(f"[+] {header} is present")



