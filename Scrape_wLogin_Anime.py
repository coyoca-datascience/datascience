# -*- coding: utf-8 -*-
import scrapy

class KissAnimeSpider(scrapy.Spider):
    name = 'KissAnime_Login'
    start_urls = ['https://www.anime-planet.com/']
    
    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                                                formdata={"username":"IfardoJohn@gmail.com", "password":"GgIfrado22-30"},
                                                callback=self.after_login)

    def after_login(self, response):
        for i in response.css('div.crop'):
            yield {
                'Anime Name':i.css('img::attr(alt)').extract_first(),
            }
    
