import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup as bs
import re

class Broodling():
    parser = 'html.parser'

    def __init__(self, url, pattern):
        """
        Job:
            crawl url using pattern
            return data to mother spider (url/ actual data IE. product info)
            terminate

        :param pattern:
                        {
                        first pattern to run: [[top level tag, action], [second level tag, action] etc, [tag that contains info, action]

                        Example for ebay search result filter: [[iterate_through_find_all,'a'],
                                                                [get, 'href'],
                                                                [filtered_yield, 'itm'],
                                                                [not_yield, 'data'],
                                                                [add links to url list]
                                                                ]
                        #the above example would iterate through list returned by find_all('a') with info next in list
                            #get "href results would be funelled to next item in list
                            #a filtered yield for itm tags would be conducted with conditions from next item in list

                        #example for next crawling step
                        get product details from links:[

                                                        ]
                        }


        :param parser:
        """

        self.soup = self.soupify(url)
        self.gen = None
        self.last_step = None
        self.current_step = None
    def set_gen(self, value):
        self.gen= value
    def get_gen(self):
        return self.gen
    def set_last_step(self, value):
        self.last_step = value
    def get_last_step(self):
        return self.last_step
    def set_current_step(self, value):
        self.current_step = value
    def get_current_step(self):
        return self.current_step
    @classmethod
    def download_url(cls, url):
        return requests.get(url).text

    @classmethod
    def soupify(cls, url):
        return bs(cls.download_url(url), 'html.parser')

    @classmethod
    def randomw_waits(cls, time_range):
        """
        cause program to wait for randomised period of time within time range
        :param time_range:
        :return:
        """
        pass

    def find_all(self, tag, soup):
        for tag in soup:
            yield tag

    def get(self, soup, tag):
        return soup.get(tag)

    def filter(self, positive, negative):
        '''
        :param positive: conditions for return
        :param negative: condition for removing from results
        :return:
        '''
        pass

    def return_to_mother(self, data):
        pass


    def crawl(self, pattern):
        funcs = {
            'find_all': self.find_all,
            'get':self.get,
            'filer': self.filter
        }
        #todo figure out how to return data to mother from seperate threads
        #   probably best to use a database do store data for everything
        #   problem comes in with storage of temp data like urls to visit
        #   potential solutions
        #       1. use in memory database for temp data
        #       2. create database that gets cleared at the end every time
        #       3. find a way to store data using python
        #   1. is probably best option
        top = pattern.pop(0)

        top_layer_tags = funcs[top[0]](top[1], self.soup)
        if str(type(top_layer_tags)) == "<class 'generator'>":
            print(type(top_layer_tags))
        for step in pattern:
            if self.get_current_step() != None:
                self.set_last_step(self.get_current_step())
                self.set_current_step(None)





class Mother_Spider():

    def __init__(self, pattern_library, store_library, search_terms,randomise_waits=False):
        """
        jobs:
            create store_search_broodling to search each website for given search term
            pair starting url with proper pattern
            create first broodling
            pair urls returned by broodling with proper patterns
            create broodlings from url/pattern combos
            repeat step 3 and 4 for every url created
            organized data returned into database
        """
        self.pattern_library = pattern_library
        self.store_library = store_library
        self.search_terms = search_terms

        if randomise_waits:
            self.randomw_waits(None)


    def spawn_broodling(self, url, pattern):
        broodling = Broodling(url, pattern)





