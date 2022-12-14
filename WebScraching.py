

import bs4
import lxml
import requests

base_url='http://books.toscrape.com/catalogue/page-{}.html'

for i in range(1,51):
    res=requests.get(base_url.format(i))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    product=soup.select(".product_pod")
    example=str(product[0])
    example1=product[0]
    if "star-rating Two" in example:
        print(str(example1.select('a')[1]['title']))
