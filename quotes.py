import requests, time, re
from bs4 import BeautifulSoup

class QuotesToScrap():


#A Constructor in python
    def __init__(self): 
        self.res = requests.get('https://quotes.toscrape.com/')
        self.soup = BeautifulSoup(self.res.content, 'html.parser')

#This Function scrapes the data from quotesToScrape website
    def scrap_data(self): 
        self.quotes = self.soup.find_all('span', class_ = 'text')
        print(self.quotes[0].text)


obj1 = QuotesToScrap()
obj1.scrap_data()