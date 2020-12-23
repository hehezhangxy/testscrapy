import scrapy
from testspider.items import TestspiderItem


class CosSpider(scrapy.Spider):
    name = 'cos'
    allowed_domains = ['dl.ixxcc.com/NSFW/Cosplay']
    start_urls = ['http://dl.ixxcc.com/NSFW/Cosplay/']

    def parse(self, response):
        filenames = response.xpath('//tr[@class="file"]//span/text()').extract()
        picsurls = response.xpath('//tr[@class="file"]//a/@href').extract()
        # urls = response.urljoin(picsurl)

        for index in range(len(filenames)):
            trueurl = response.urljoin(picsurls[index])

            print(filenames[index])
            print(trueurl)
            yield scrapy.Request(url=trueurl, meta={'filename': filenames[index]}, callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        filename = response.meta['filename']
        print(filename)
        picnames = response.xpath('//tr[@class="file"]//a//span/text()').extract()

        urls = response.xpath('//tr[@class="file"]//a/@href').extract()
        for index in range(len(picnames)):
            print(picnames[index])
            downloadurl = response.urljoin(urls[index])
            print(downloadurl)
