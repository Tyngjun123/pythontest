import scrapy

class LocalhostSpider(scrapy.Spider):
    name = "localhost_spider"
    start_urls = ['http://127.0.0.1:5000/']

    def parse(self, response):
        # Extract the title
        title = response.xpath('//title/text()').get()

        # Extract the heading (h1 tag)
        heading = response.xpath('//h1/text()').get()

        # Extract the paragraph (p tag)
        paragraph = response.xpath('//p/text()').get()

        # Return the extracted data as a dictionary
        yield {
            'title': title,
            'heading': heading,
            'paragraph': paragraph,
        }
