import scrapy


class CosSpider(scrapy.Spider):
    name = 'cos'
    allowed_domains = ['dl.ixxcc.com/NSFW/Cosplay']
    start_urls = ['http://dl.ixxcc.com/NSFW/Cosplay/']

    def parse(self, response):
        pass
