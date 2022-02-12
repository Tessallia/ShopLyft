import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import re

class crawler:

    def __init__(self):
        self.urls_to_check = []
        self.subrawling = []

    def download_url(self, url):
        return requests.get(url).text

    def weedout(self, text, filter):
        for con in filter:
            if con in text.lower():
                return False
        return True
    def weedin(self, text, filter):
        for con in filter:
            if con in text.lower():
                return True
        return False

    def soupify(self, url):
        return BeautifulSoup(self.download_url(url), 'html.parser')
    def search_results(self, url):

        soup = self.soupify(url)
        tellme = open('soup.txt', 'w')
        ign = ['data']
        for a in soup.find_all('a'):
            h = a.get('href')
            if h:
                if self.weedin(h, ['itm']):
                    if self.weedout(h, ign):
                        yield h


    def crawlingInMySkin(self, url):
        for shit in self.search_results(url):
            if shit not in self.urls_to_check:
                self.urls_to_check.append(shit)
                print(sub_crawller(self.soupify(shit)).ret_data())
class sub_crawller():
    def __init__(self, soup):
        self.title = self.get_title(soup)
        self.price = self.get_price(soup)
        self.itmatr = self.conv_itmatr_dict(self.get_itmatr(soup))

    def ret_data(self):
        return [self.title, self.price, self.itmatr]

    def get_title(self, soup): return soup.find('span', {'id': 'vi-lkhdr-itmTitl'}).text
    def get_price(self, soup): return soup.find('span', {'class': 'notranslate'}).text

    def get_itmatr(self, soup):
        for x in soup.find('div', {'id': 'viTabs_0_is'}).find_all(['td']):
            yield re.sub("\n", '',x.text.strip())

    def conv_itmatr_dict(self, itmatr):
        item_dict = {}
        last_key = None
        for atr in itmatr:
            if atr[-1] == ":":

                last_key = atr
                item_dict[atr] =None
            else:
                item_dict[last_key]=atr
        return item_dict

    def get_product_details(self, url):
        soup = self.soupify(url)
        self.title=self.get_title(soup).text
        self.price=self.get_price(soup).text
        self.itmatr = self.conv_itmatr_dict(self.get_itmatr(soup))
        print(self.title)



        #for key, val in details.items():
        #    if key not in self.keys:
        #        self.common_keys.append(key)



link = '''https://www.ebay.com/sch/i.html?_from=R40&_nkw=ubiquiti+edge+router&_sacat=0&_ipg=25'''
#link2 = """https://www.ebay.com/itm/164934779776?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2055359.m1431.l2649"""
#link3 = """https://www.ebay.com/itm/274811487666?epid=28032167316&hash=item3ffc0a85b2:g:C~IAAOSw5VdgrpEm"""

if __name__ == "__main__":
    crawdaddy = crawler()
    crawdaddy.crawlingInMySkin(link)
