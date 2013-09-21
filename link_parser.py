import re


class LinkParser(object):

    def __init__(self):
        self.pattern = re.compile('< *a[^>]+href=\"([^\"]+\\.htm)\"[^>]*>')

    def parse_content(self, content):
        """
        extract urls from the content
        :param content: the content of a html file
        :return a collection of urls
        """

        urls = self.pattern.findall(content)

        return [url for url in set(urls) if self.is_valid(url)]

    def is_valid(self, url):
        """
        check whether url is in the form we specified
        :param url: url string
        :return : True if it is valid or False
        """
        if url.startswith('http') or url.startswith('www'):
            return False

        else:
            return True

    def build_url(self, root, url):
        """
        build the full path of the url
        :param root: root path
        :param url: current url
        """
        level = url.count('..')
        index1 = 0
        index2 = 0
        i = 0
        start = 0
        end = len(root)

        while i < level+1:
            index1 = root.rfind('/', 0, end)
            end = index1 - 1
            i += 1

        i = 0
        while i < level:
            index2 = url.find('../', index2)
            index2 += 3
            i += 1

        return root[0:index1+1] + url[index2:]