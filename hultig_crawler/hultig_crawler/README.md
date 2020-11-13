# Scrapy Tutorial

This is tutorial for using the HultigCrawler, A text crawler based on scrapy and beautifulsoap4 with MySQL as backend.



## Setup
Tested with Python 3.8.5 :

## install dependencies present in hultig_crawler folder, i,e; hultig_crawler\hultig_crawler\requirements.txt
pip install requirements.txt

## Create Database and table in MySQL:

	CREATE TABLE IF NOT EXISTS hultig_crawler(
		`ID` bigint(20) AUTO_INCREMENT NOT NULL,
		`URL` varchar(255) NOT NULL,
		`Title` varchar(255) NOT NULL,
		`Tags` varchar(255) ,
		`Text` longtext ,
    	`Time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
		PRIMARY KEY (id)
    	)

## configure database settings in hultig_crawler\hultig_crawler\pipelines.py :
    
    table = 'hultig_crawler'
    conf = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'database': 'hultigcrawler',
        'raise_on_warnings': True
    }

## Run

Run `scrapy crawl hultig_crawler` at the project top level. i,e; hultig_crawler\

Note that spider name is defined in the spider class, e.g., `text_crawler.py`:
```python
class TextCrawlerSpider(CrawlSpider):

    name = 'hultig_crawler'
```

