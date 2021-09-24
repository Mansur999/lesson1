import requests
import bs4

class Client:
    def __init__(self):
        self.session = requests.session();
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Accept - Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'}

    def loadPage(self):
        url = ''
        res = self.session.get(url)
        res.raise_for_status()
        return res.text

    def parsePage(self,text: str):
        soup = bs4.BeautifulSoup(text,'lxml')
        temp = soup.select('div.product-card.j-card-item.j-advert-card-item.advert-card-item')
        for block in temp:
            self.parseBlock(block=block)

    def parseBlock(self,block):
        print(block)