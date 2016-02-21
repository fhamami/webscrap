"""
simple web scraping
"""

import requests
from bs4 import BeautifulSoup

url = raw_input("input url :")
tag1 = raw_input("Pada tag Masukkan HTML tag :")
# tag2 = raw_input("Pada tag1 Masukkan HTML tag seperti div/li/span ,etc :")
# tag3 = raw_input("Pada tag1 Masukkan HTML tag seperti div/li/span ,etc :")

r = requests.get(url)

soup = BeautifulSoup(r.content)

#links = soup.find_all("a")
# g_data = soup.find_all(tag1, {tag2: tag3})
g_data = soup.find_all(tag1)

for link in g_data:
	print link.text