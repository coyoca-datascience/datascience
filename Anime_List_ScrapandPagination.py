# -*- coding: utf-8 -*-
import scrapy


class Anime_List_ScrapandPaginationSpider(scrapy.Spider):
    
    page_number = 50
    name            = 'Anime_List_ScrapandPagination'
    start_urls      = ['https://myanimelist.net/topanime.php?limit=0']

    def parse(self, response):
        
        for data in response.css('.ranking-list'):
            yield {
                'Anime Number':data.css('td.rank>span::text').extract_first(),
                'Anime Title':data.css('div.di-ib>a::text').extract_first(),
                'Anime Details':data.css('div.information').extract(),
                'Anime Ranking':data.css('div.js-top-ranking-score-col>span::text').extract_first()
                }
                
        next_page = 'https://myanimelist.net/topanime.php?limit=' + str(Anime_List_ScrapandPaginationSpider.page_number)
        if Anime_List_ScrapandPaginationSpider.page_number < 101:
            Anime_List_ScrapandPaginationSpider.page_number +=50
            yield response.follow(next_page, callback=self.parse)
    
        
