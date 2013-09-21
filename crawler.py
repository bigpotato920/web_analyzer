import urllib
import time
from collections import deque
from link_parser import LinkParser
from web_graph import WebGraph


class Crawler(object):
    def __init__(self):
        self.url_queue = deque()
        self.lp = LinkParser()
        self.wg = WebGraph()

    def insert_root(self, root):
        self.url_queue.append(root)

    def do_crawl(self):

        while True:
            try:
                root = self.url_queue.popleft()
            except IndexError:
                print 'done ....'
                break

            opener = urllib.urlopen(root)
            status = opener.getcode()

            if status == 200:

                content = opener.read()
                urls = self.lp.parse_content(content)
                urls = [self.lp.build_url(root, url) for url in urls]

                self.wg.insert_vertex(root)

                for url in urls:
                    self.wg.insert_edge(root, url)
                    if not self.wg.has_vertex(url):
                        self.url_queue.append(url)

            opener.close()

        print time.ctime()

        self.wg.cal_pagerank(0.15, 0.001)

