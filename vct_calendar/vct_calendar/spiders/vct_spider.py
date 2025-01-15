import scrapy


class VctSpiderSpider(scrapy.Spider):
    name = "vct_spider"
    allowed_domains = ["valorantesports.com"]
    start_urls = ["https://valorantesports.com"]

    def parse(self, response):
        pass
