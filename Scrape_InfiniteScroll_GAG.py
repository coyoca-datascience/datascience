# -*- coding: utf-8 -*-
import scrapy
import json


class gagScrapeSpider(scrapy.Spider):
    name = 'Scrape_gag'
    gag_base_url = 'https://9gag.com/v1/group-posts/group/default/type/hot?after=aAgEYpR%2Cad5O6Vj%2CaroAp90&c={}'
    start_urls = [gag_base_url.format(10)]
    download_delay = 1.5

    def parse(self, response):
        
        for i in range(20):
            json_data = json.loads(response.text)
            for posts in json_data['data']['posts']:
                yield {
                    'Id':posts['id'],
                    'URL':posts['url'],
                    'Title':posts['title'],
                }
            
            if json_data['meta']['status'] == 'Success' :
                yield scrapy.Request(self.gag_base_url + str(10) )

