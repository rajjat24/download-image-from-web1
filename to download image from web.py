import random
import urllib.request


def downloadweb(url):
    name=random.randrange(1,1000)
    fullname=str(name)+".jpeg"
    urllib.request.urlretrieve(url,fullname)
downloadweb("https://www.almanac.com/sites/default/files/styles/primary_image_in_article/public/image_nodes/sunflower-1627193_1920.jpg?itok=ua6taclY")