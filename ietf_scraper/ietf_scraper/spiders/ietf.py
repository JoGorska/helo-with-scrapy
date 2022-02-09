import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author = response.xpath('//span[@class="author-name"]/text()').get()
        # author = response.xpath('//meta[@name="DC.Creator"]/@content').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        subtitle = response.xpath('//span[@class="subheading"]/text()').getall()
        return {
            "title": title,
            "author": author,
            "date": date,
            "subtitle": subtitle
            }
