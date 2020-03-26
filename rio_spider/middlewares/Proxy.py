import random

'''
    Middleware: 代理随机Proxy 
'''


class MyProxyMiddleware(object):

    def __init__(self, ip):
        self.ip = ip

    @classmethod
    def from_crawler(cls, crawler):
        return cls(ip=crawler.settings.get('PROXIES'))

    def process_request(self, request, spider):
        ip = random.choice(self.ip)
        request.meta['proxy'] = ip

    # def process_response(self,request,response):
    #     pass