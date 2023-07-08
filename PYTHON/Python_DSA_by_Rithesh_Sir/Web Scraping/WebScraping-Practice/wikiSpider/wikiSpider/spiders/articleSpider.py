# from scrapy.selector import Selector
# from scrapy import Spider
# from wikiSpider.items import Article

# class ArticleSpider(Spider):
#     name = "article"
#     allowed_domains = ["en.wikipedia.org"]
#     start_urls = ["http://en.wikipedia.org/wiki/Main_Page","https://en.wikipedia.org/wiki/Python_(programming_language)"]

#     def parse(self,response):
#         item = Article()
#         title = response.xpath('//h1/span/text()')[0].extract()
#         print("Title is :"+title)
#         item['title'] = title
#         return item


from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider1(CrawlSpider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item",follow=True)]

    def parse_item(self,response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is :"+title)
        item['title'] = title
        return item