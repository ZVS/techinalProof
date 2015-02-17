# -*- coding: UTF-8 -*-

__author__ = 'welcomebaek'

from bs4 import BeautifulSoup
import requests

class ridiSearch:

    #rtnResult = ['title','author','img_link','sell_link','publisher','price']
    rtnResult=[]


    def __init__(self):
        return

    def search(self, key):
        #request query to ridibooks
        payload = {'q': key}
        url = 'http://ridibooks.com/search'
        resreq = requests.get(url=url, params=payload)

        soup = BeautifulSoup(resreq.text)

        booksinfo = soup.find_all('div', ['book_wrapper'])



        #iter through book information
        for iter in booksinfo:
            rtnTitle=iter.find('span', ['title_text']).text
            rtnImg=iter.img['data-original']
            rtnLink=iter.a['href']
            rtnPub=iter.find('li', ['publisher']).a.text
            rtnPrice=iter.find('span', ['price']).text
            rtnAuthor=iter.find('li', ['author']).a.text
            self.rtnResult.append([rtnTitle, rtnImg, rtnAuthor, rtnPub, rtnPrice, rtnLink])


        return self.rtnResult



#test code
def main():
    rsearch=ridiSearch()

    res=rsearch.search('정의란')
    for iters in res:
        s=iters[0]
        s=s.strip()
        print s


if __name__=='__main__':
    main()


