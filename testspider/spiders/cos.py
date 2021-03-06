import scrapy
from testspider.items import TestspiderItem


class CosSpider(scrapy.Spider):
    name = 'cos'
    allowed_domains = ['dl.ixxcc.com/NSFW/Cosplay']
    start_urls = ['http://dl.ixxcc.com/NSFW/Cosplay/']

    def parse(self, response):
        foldernames = response.xpath('//tr[@class="file"]//span/text()').extract()
        picsurls = response.xpath('//tr[@class="file"]//a/@href').extract()

        for index in range(len(foldernames)):
            trueurl = response.urljoin(picsurls[index])

            yield scrapy.Request(url=trueurl, meta={'folder_name': foldernames[index]}, callback=self.parse2,
                                 dont_filter=True)

    def parse2(self, response):
        folder_name = response.meta['folder_name']
        # 文件真实名字集合
        # picnames = response.xpath('//tr[@class="file"]//a//span/text()').extract()

        urls = response.xpath('//tr[@class="file"]//a/@href').extract()
        for index in range(len(urls)):
            url = urls[index]
            urls[index] = response.urljoin(url)
        yield TestspiderItem(folder_name=folder_name, image_urls=urls)
