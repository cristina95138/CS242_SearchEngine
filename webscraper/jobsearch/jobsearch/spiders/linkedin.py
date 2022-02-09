import scrapy
import logging

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['www.linkedin.com']
    start_urls = ['https://www.linkedin.com/jobs/search/']

    def parse(self, response):
        job_links = response.xpath("//li/div/a")

        for job_link in job_links:
            link = job_link.xpath("./@href").get()
            yield response.follow(url=link, callback=self.parse_job)

        # yield {
        #     'job_links': link,
        # }


    def parse_job(self, response):
        company_name = response.xpath("//h4/div/span/a/text()").get()
        job_title = response.xpath("//div/div/h1/text()").get()
        description = response.xpath("//div/div/section/div/text()").get()
        related_jobs = response.xpath("//main/section/div/section/div/div/ul")

        for related_job in related_jobs:
            link = related_job.xpath("./@href").get()
            print(link)
            yield response.follow(url=link, callback=self.parse_job)

        # yield {
        #     'company': company_name,
        #     'title': job_title,
        #
        # }
