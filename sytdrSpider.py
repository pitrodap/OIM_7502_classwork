import scrapy


class SytdrspiderSpider(scrapy.Spider):
    name = "sytdrSpider"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        tbody = response.xpath("//div[@class='row']//div[@class='table-responsive']/table/tbody")

        # Extracting data from each row of the table
        for row in tbody.xpath("./tr"):
            numb = row.xpath('./td[1]/text()').get()
            company = row.xpath('./td[2]/a/text()').get()
            symbol = row.xpath('./td[3]/a/text()').get()
            ytdret = row.xpath('./td[4]/text()').get()

            yield {"Number": numb, "Company": company, "Symbol": symbol, "YTD Return": ytdret}
