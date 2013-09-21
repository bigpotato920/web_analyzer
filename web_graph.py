import time


class WebGraph(object):

    def __init__(self):
        self.graph = {}
        self.graph.fromkeys((range(400000)))
        self.count = 0

    def has_vertex(self, url):
        return url in self.graph.keys()

    def insert_vertex(self, url):
        self.graph[url] = []
        self.count += 1
        if self.count % 1000 == 0:
            print self.count, time.ctime()

    def insert_edge(self, src, dst):
        self.graph[src].append(dst)
        pass

    def refer_pages(self, dst):
        for src in self.graph.keys():
            return [src for dst in self.graph[src]]

    def cal_pagerank(self, damping_factor, min_delta):
        keys = self.graph.keys()
        min_value = (1.0 - damping_factor) / len(keys)
        pagerank = dict.fromkeys(keys, len(keys))

        while True:
            diff = 0
            for node in keys:
                rank = min_value
                for refer_page in self.refer_pages(node):
                    rank += damping_factor*pagerank[refer_page]/len(self.graph[refer_page])
                diff += abs(pagerank[node] - rank)
                pagerank[node] = rank
            if diff < min_delta:
                break

        return pagerank[0:10]

    def show(self):
        for src in self.graph:
            for dst in self.graph[src]:
                print src,'---->',dst

