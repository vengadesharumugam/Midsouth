#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy

class MidsouthSpider(scrapy.Spider):
    
    name = 'midsouth'

    
    allowed_domains = ['midsouthshooterssupply.com/dept/reloading/primers']

    
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers']

    
    custom_settings = {
        'FEED_URI' : 'tmp/midsouth.csv'
    }

    def parse(self, response):
        
        response.selector.remove_namespaces()

        
        price = response.xpath('//item/price/text()').extract()
        description = response.xpath('//item/description/text()').extract()
        review = response.xpath('//item/review/text()').extract()
        delivery_info= response.xpath('//item/delivery-info/text()').extract()
        title = response.xpath('//item/title/text()').extract()
        stock_status = response.xpath('//item/stock-status()').extract()
        manufacturer = response.xpath('//item/Manufacturer()').extract()

        for item in zip(price,description,review,delivery_info,title,stock_status,manufacturer):
            scraped_info = {
                'price' : item[0],
                'description' : item[1],
                'review' : item[2],
                'delivery_info' : item[3]
                'title' : item[4]
                'stock_status' : item[5]
                'manufacturer' : item[6]
            }

            yield scraped_info


# In[ ]:




