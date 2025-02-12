import requests, time, re
from bs4 import BeautifulSoup

class QuotesToScrap():


#A Constructor in python
    def __init__(self): 
        self.quotes_list = []
        self.authors_list = []
        self.tags_list = []

#This Function scrapes the data from quotesToScrape website
    def scrap_data(self):
        for i in range(1,11):
            self.res = requests.get(f'https://quotes.toscrape.com/page/{i}/')
            self.soup = BeautifulSoup(self.res.content, 'html.parser')

            self.quotes = self.soup.find_all('span', class_ = 'text')
            self.author = self.soup.find_all('small', class_ = 'author')
            self.tags = self.soup.find_all('div', class_ = 'tags')
            
            for a,b,c in zip(self.quotes, self.author, self.tags):
                self.quotes_list.append(a.text)
                self.authors_list.append(b.text)
                self.tags_list.append(b.text)
        


obj1 = QuotesToScrap()
obj1.scrap_data()
print(obj1.quotes_list)