import scrapy
#import jsons
from new.items import flipkart
#from project_name.kafka.kafka_service import send_data_to_kafka_topic


class FlipkartProductSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    base_url = 'https://www.flipkart.com'
    start_urls = ['https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&otracker=categorytree&page=1']

    def parse(self, response):
        all_products = response.xpath('.//div[@class="_3liAhj"]')

        for product in all_products:
            product_url = product.xpath('.//a/@href').extract_first()
            product_url = self.base_url + product_url
            #print('Product url :', product_url)
            yield scrapy.Request(product_url, callback=self.parse_product)

        next_page = response.xpath('.//a[@class="_2Xp0TH"]/@href').extract()
        for link in range(len(next_page)):
            if link == 50:
                break
            yield scrapy.Request(response.urljoin(next_page[link]), callback=self.parse)

    def parse_product(self, response):
        item = flipkart()
        item['product_name'] = response.xpath('.//span[@class="_35KyD6"]/text()').extract_first()
        item['price'] = response.xpath('.//div[@class="_1vC4OE _3qQ9m1"]/text()').extract_first()
        #send_data_to_kafka_topic('test', jsons.dumps(item).encode('utf-8'))
        return item
