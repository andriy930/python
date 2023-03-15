# scrapy runspider textPy.py
import scrapy

class SesameSpider(scrapy.Spider):
    name = 'sesameSpider'
    start_urls = ['https://panel.sesametime.com/']

    user_name = '***'
    pass_wd = '***'

    def parse(self, response):
        token_CSRF = response.css("form input[name='data[_Token][key]']::attr(value)").get()
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                'data[_Token][key]': token_CSRF, 
                'data[User][email]': self.user_name,
                'data[User][password]': self.pass_wd
            },
            callback=self.do_check
        )

    def do_check(self, response):
        url_check = response.css("a#check_button::attr(href)").get()
        yield scrapy.FormRequest(response.urljoin(url_check))

