from crawler import Crawler

import time

print time.ctime()

crawler = Crawler()
crawler.insert_root("http://localhost:80/techqq/index.html")
crawler.do_crawl()

print time.ctime()





