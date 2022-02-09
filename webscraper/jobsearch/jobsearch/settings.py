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


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobsearch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

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
208.52.157.15:5555
134.209.178.70:8890
184.95.0.218:8080
50.206.25.106:80
18.214.224.179:80
20.47.108.204:8888
23.224.128.101:59394
35.187.224.178:3128
74.208.181.171:5050
157.230.233.189:3005
67.219.112.233:8080
67.73.245.218:999
162.217.248.126:3128
167.71.5.83:8080
137.220.176.235:8080
209.97.150.167:8080
152.228.163.151:80
162.55.163.151:80
167.86.81.208:3128
157.245.42.142:80
35.210.27.183:80
47.243.228.222:59394
50.206.25.104:80
20.74.176.103:8080
107.151.182.247:80
34.138.225.120:8888
216.137.184.253:80
167.71.5.83:3128
72.80.242.101:8080
47.56.69.11:8000
191.96.42.80:8080
130.185.119.20:3128
47.243.68.117:8080
98.115.7.156:8080
67.219.116.69:8080
208.52.157.22:5555
20.103.139.62:3128
161.97.85.97:80
20.94.230.158:80
98.154.21.253:3128
50.206.25.110:80
52.250.1.188:80
65.20.178.15:8080
135.125.244.181:3128
161.97.177.130:3128
18.218.204.62:80
208.52.137.186:5555
47.243.135.104:8080
157.90.251.43:80
159.65.69.186:9300
98.12.195.129:443
50.206.25.109:80
206.84.99.202:8085
206.62.64.34:8080
69.160.192.139:8080
209.97.150.167:3128
107.151.182.254:80
38.130.248.182:999
198.244.138.126:3128
208.52.137.150:5555
67.55.186.162:8080
206.84.99.203:8085
208.52.157.22:6556
191.96.42.80:3128
70.186.128.126:8080
96.36.8.51:8080
20.105.253.176:8080
68.185.57.66:80
34.65.131.94:443
34.140.87.13:80
159.65.171.69:80
161.97.179.49:3128
50.233.42.98:51696
179.61.229.164:999
207.183.185.36:8009
75.119.146.236:6969
24.113.42.177:48678
208.87.134.254:80
47.242.230.213:12345
50.235.149.74:8080
162.223.89.77:9090
96.2.228.18:8080
69.65.65.178:58389
34.229.168.95:8118
47.57.138.120:12311
52.128.59.201:8080
138.68.60.8:3128
50.206.25.111:80
34.146.157.204:9090
38.10.246.19:999
150.136.139.184:443
38.9.162.127:999
192.154.249.223:8000
204.199.67.174:999
23.224.127.14:59394
23.224.20.134:8080
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
