# Yugioh Card Price Checker
# This is a script to track the price of Yugioh cards
# Author: sevenlamps

import scrapy


class YgoSpider(scrapy.Spider):
    name = 'ygospider'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://www.bigweb.co.jp/ver2/yugioh_index.php',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)



