

import bs4
import lxml
import requests
two_star_titles=[]
base_url='http://books.toscrape.com/catalogue/page-{}.html'

for i in range(1,51):
    res=requests.get(base_url.format(i))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two '))!=0:
            book_title=(book.select('a')[1]['title'])
            two_star_titles.append(book_title)
print(two_star_titles)