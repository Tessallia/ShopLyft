import requests
from Brood.Broodling import Broodling, Mother_Spider

def get_robots(url):
    if not url.startswith('http://'):
        url = 'http://'+url
    text = requests.get(url+"/robots.txt")
    return text.content



if __name__ == '__main__':
    link = '''https://www.ebay.com/sch/i.html?_from=R40&_nkw=ubiquiti+edge+router&_sacat=0&_ipg=25'''

    pattern = [
        ['find_all', 'a'],
        ['get', 'href'],
        ['filter', ['itm'], ['data']],

    ]

    mother = Mother_Spider(pattern, [], "")

    spooder = Broodling(url=link, pattern=pattern)
    spooder.crawl(pattern)

    #print([f for f in dir (Spider) if not f.startswith('_')])
    #t = get_robots('amazon.com').splitlines()
    #for x in t:
    #    if str(x).startswith("b'Allow"):
    #        print(x)
