import scrapy
import logging

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['www.linkedin.com/jobs']
    start_urls = ['https://www.linkedin.com/jobs/search/']

    def parse(self, response):
        job_links = response.xpath("//li/div/a")

        for job_link in job_links:
            link = job_link.xpath("./@href").get()
            print(link)
            yield response.follow(url=link, callback=self.parse_job)

        # yield {
        #     'job_links': link,
        # }


    def parse_job(self, response):
        company_name = response.xpath("//div/span/a/text()")
        print(company_name)
        job_title = response.xpath("//div/span/a/text()")
        print(job_title)
        description = response.xpath("//div/div/h1/text()")

        yield {
            'company': company_name,
            'title': job_title,
        }
