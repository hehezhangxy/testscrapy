import scrapy
from testspider.items import TestspiderItem


class CosSpider(scrapy.Spider):
    name = 'cos'
    allowed_domains = ['dl.ixxcc.com/NSFW/Cosplay']
    start_urls = ['http://dl.ixxcc.com/NSFW/Cosplay/']

    def parse(self, response):
        filenames = response.css('.file')
        for name in filenames:
            item = TestspiderItem()
            item['filename'] = name.css('.name::text').extract_first()
            yield item
