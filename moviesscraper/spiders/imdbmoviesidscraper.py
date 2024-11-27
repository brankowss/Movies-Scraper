import scrapy
import json

class ImdbmoviesidscraperSpider(scrapy.Spider):
    name = "imdbmoviesidscraper"
    allowed_domains = ["https://www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        
        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()

        json_data = json.loads(raw_data)

        needed_data = json_data['props']['pageProps']['pageData']['chartTitles']['edges']

        for movie in needed_data:
            yield {
                'id': movie['node']['id']
            }
