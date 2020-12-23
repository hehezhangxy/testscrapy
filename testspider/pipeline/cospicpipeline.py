from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import testspider.settings as settings
import os


class CosPicPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(url=u, meta={"folder_name": item['folder_name']}) for u in urls]
        # return super().get_media_requests(item, info)

    def file_path(self, request, response=None, info=None, *, item=None):
        path = super().file_path(request, response, info, item=item)
        folder_name = response.meta['folder_name']

        store_path = os.path.join(settings.IMAGES_STORE, folder_name)
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        image_name = path.replace('full/', '')
        return os.path.join(store_path, image_name)
