# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import testspider.settings as settings
import os


class TestspiderPipeline:
    def process_item(self, item, spider):
        return item


class CosPicPipeLine(ImagesPipeline):

    def __init__(self, store_uri, download_func=None, settings=None):
        print('start')
        super().__init__(store_uri, download_func, settings)

    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        for request in requests:
            request.item = item
        return requests

    def file_path(self, request, response=None, info=None, *, item=None):
        path = super().file_path(request, response, info, item=item)
        folder_name = request.item.get('folder_name')

        store_path = os.path.join(settings.IMAGES_STORE, folder_name)
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        image_name = path.replace("full/", "")
        true_url = os.path.join(store_path, image_name)
        return true_url
