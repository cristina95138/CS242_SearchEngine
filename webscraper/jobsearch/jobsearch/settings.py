# Scrapy settings for jobsearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jobsearch'

SPIDER_MODULES = ['jobsearch.spiders']
NEWSPIDER_MODULE = 'jobsearch.spiders'

LOG_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobsearch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jobsearch.middlewares.JobsearchSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jobsearch.middlewares.JobsearchDownloaderMiddleware': 543,
#}

ROTATING_PROXY_LIST = [
    '134.209.216.204:3130',
    '12.218.209.130:53281',
    '50.24.123.86:8118',
    '47.88.15.217:80',
    '45.79.230.234:80',
    '64.185.0.17:8080',
    '23.224.128.101:59394',
    '67.205.128.38:3128',
    '96.2.228.18:8080',
    '184.155.36.194:8080',
    '20.47.108.204:8888',
    '209.141.55.228:80',
    '20.94.230.158:80',
    '205.185.122.11:80',
    '209.141.35.151:80',
    '74.84.144.135:80',
    '134.122.26.172:3128',
    '66.94.97.238:443',
    '191.96.42.80:8080',
    '199.19.225.250:80',
    '199.19.224.3:80',
    '149.19.224.37:3128',
    '205.201.49.131:53281',
    '74.143.245.221:80',
    '138.68.60.8:8080',
    '99.71.86.199:8118',
    '185.101.97.24:8118',
    '23.108.43.53:8118',
    '23.108.43.123:8118',
    '23.108.42.251:8118',
    '23.108.42.70:8118',
    '35.152.75.76:8263',
    '68.188.59.198:80',
    '149.19.224.37:3128',
    '67.73.245.220:999',
    '208.52.157.15:5555',
    '134.209.178.70:8890',
    '184.95.0.218:8080',
    '50.206.25.106:80',
    '18.214.224.179:80',
    '20.47.108.204:8888',
    '23.224.128.101:59394',
    '35.187.224.178:3128',
    '74.208.181.171:5050',
    '157.230.233.189:3005',
    '67.219.112.233:8080',
    '67.73.245.218:999',
    '162.217.248.126:3128',
    '167.71.5.83:8080',
    '137.220.176.235:8080',
    '209.97.150.167:8080',
    '152.228.163.151:80',
    '162.55.163.151:80',
    '167.86.81.208:3128',
    '157.245.42.142:80',
    '35.210.27.183:80',
    '47.243.228.222:59394',
    '50.206.25.104:80',
    '20.74.176.103:8080',
    '107.151.182.247:80',
    '34.138.225.120:8888',
    '216.137.184.253:80',
    '167.71.5.83:3128',
    '72.80.242.101:8080',
    '47.56.69.11:8000',
    '191.96.42.80:8080',
    '130.185.119.20:3128',
    '47.243.68.117:8080',
    '98.115.7.156:8080'
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jobsearch.pipelines.JobsearchPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
