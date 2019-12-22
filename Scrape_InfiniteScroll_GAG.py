# -*- coding: utf-8 -*-
import scrapy
import json

n = 0

class gagScrapeSpider(scrapy.Spider):
    name = 'Scrape_gag'
    gag_base_url = 'https://9gag.com/v1/group-posts/group/default/type/hot?after=aAgEYpR%2Cad5O6Vj%2CaroAp90&c={}'
    start_urls = [gag_base_url.format(10)]
    download_delay = 1.5
    
    def parse(self, response):
        global n
        if n < 500:
            json_data = json.loads(response.text)
            for posts in json_data['data']['posts']:
                yield {
                    'Id':posts['id'],
                    'URL':posts['url'],
                    'Title':posts['title'],
                }
            
            if json_data['meta']['status'] == 'Success' :
                n += 10
                yield scrapy.Request(url=self.gag_base_url.format(n),callback=self.parse)

