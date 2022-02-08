import scrapy
import logging

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['www.linkedin.com/jobs']
    start_urls = ['https://www.linkedin.com/jobs/search/']

    def parse(self, response):
        job_links = response.xpath("//td/a").getall()

        for job_link in job_links:
            link = job_link.xpath(".//@href").get()

        yield {
            'job_links': job_links,
        }

        # yield response.follow(url=link, callback=self.parse_country)
        #
        # pass

    def parse_job(self, response):
        company_name = response.request
        logging.info(response.url)
