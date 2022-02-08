import scrapy
import logging

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['https://www.linkedin.com/jobs/search/']
    start_urls = ['http://https://www.linkedin.com/jobs/search//']

    def parse(self, response):
        jobs = response.xpath("").getall()

        for job in jobs:
            name = job.xpath("").get()
            link = job.xpath("").get()

        yield {
            'jobs': jobs,
            'job_name': name,
            'job_link': link,
        }

        yield response.follow(url=link, callback=self.parse_country)

        pass

    def parse_job(self, response):
        logging.info(response.url)
