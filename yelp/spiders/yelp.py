from scrapy import Spider
from yelp.items import YelpItem
import scrapy
import re 


class YelpSpider(Spider):
    name = "yelp"
    allowed_domains = ['www.yelp.com']
    # Defining the list of pages to scrape
    start_urls = ["https://www.yelp.com/search?find_desc=Dog&find_loc=Boston%2C%20MA&start=" + str(10 * i) for i in range(0, 1)] 
    handle_httpstatus_list = [302]


    def parse(self, response):
        # Defining rows to be scraped
        rows = response.xpath('//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li')
        for row in rows:
            
            # Scraping Busines' Name
            name = row.xpath('.//p/a/text()').extract_first()
            
            # Scraping Phone number
            phone = row.xpath('.//div[1]/p[1][@class= "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7"]/text()').extract_first()
            
            # scraping area
            area = row.xpath('.//p/span[@class = "lemon--span__373c0__3997G"]/text()').extract_first()
            
            # Scraping services they offer
            services = row.xpath('.//a[@class="lemon--a__373c0__IEZFH link__373c0__29943 link-color--inherit__373c0__15ymx link-size--default__373c0__1skgq"]/text()').extract_first()
            
            # Extracting internal link
            link = row.xpath('.//p/a/@href').extract_first()
            link = response.urljoin(link)
            

           
            item = YelpItem()    
            item['name'] = name
            item['phone'] = phone
            item['area'] = area
            item['services'] = services
            item['link'] = link


            yield item

        def parse_detail(self, response):
            item = response.meta['item']
            address = response.xpath('.//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div/div[2]/ul/li[1]/div/strong/address/text()[1]').extract_first()
            
            website = response.xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div/div[2]/ul/li[4]/span[2]/a/@href').extract_first()
            website = response.urljoin(website)

            item['address'] = address
            item['website'] = website
            yield item