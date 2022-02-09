from bs4 import BeautifulSoup
from itertools import product
import scrapy

class IndeedSpider(scrapy.Spider):
    job_titles = ["Medical", "Engineer", "Teacher", "Supervisor", "Manager", "Assistant", "Lawyer", "Developer", "Nurse", "Office", "Worker", "Officer", "Specialist", "Sale", "Representative", "Cashier", "Clerk", "Secretary"]
    countries = ["USA"]
    urls = []
    for (job_title, country) in product(job_titles, countries):
        urls.append(f"https://www.indeed.com/q-{'-'.join(job_title.split())}-l-{country}-jobs.html")

    name = "indeed"
    allowed_domains = ["www.indeed.com"]
    start_urls = urls

    def parse_jd(self, response, **posting):
        soup = BeautifulSoup(response.text, features="lxml")
        jd = soup.find("div", {"id": "jobDescriptionText"}).get_text()
        url = response.url
        posting.update({"job_description": jd, "url": url})
        yield posting

    def parse(self, response):
        soup = BeautifulSoup(response.text, features="lxml")

        listings = soup.find_all("a", {"class": "tapItem"})
        for listing in listings:
            title = listing.find("h2", {"class": "jobTitle"}).get_text().strip()
            summary = listing.find("div", {"class": "job-snippet"}).get_text().strip()
            company = listing.find("span", {"class": "companyName"}).get_text().strip()
            location = listing.find("div", {"class": "companyLocation"}).get_text().strip()

            posting = {"job_title": title, "summary": summary, "company": company, "location": location}
            page = listing.get("href")
            if page is not None:
                yield response.follow(page, callback=self.parse_jd, cb_kwargs=posting)

        next_page = soup.find("a", {"aria-label": "Next"}).get("href")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)