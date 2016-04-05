import re
import json
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from ttmeiju_findlist.items import *

class ttmeijufindlistSpider(CrawlSpider):
    name = "ttmeiju_findlist"
    allowed_domains = ["ttmeiju.com"]
    start_urls = ["http://www.ttmeiju.com/summary.html"]
    rules = [Rule(sle(allow=("/summary.html")),follow=True,callback='parse_items')]
    print rules
    def parse_items(self,response):
        res = []
        print response
        sel = Selector(response)
        base_url = get_base_url(response)
        for site in response.xpath('//tr[contains(@bgcolor,"#ffffff")]'):
            item = TtmeijuFindlistItem()
            info = site.xpath('.//td')
            item['name_meiju'] = info[1].xpath('.//a/text()').extract()
            item['link_meiju'] = info[1].xpath('.//a/@href').extract()
            # item['namel'] = info[1].xpath('.//a/text()').extract()
            # item['link'] = info[2].xpath('.//a/@href').extract()
            # item['size'] = info[3].xpath('./text()').extract()
            # item['format'] = info[4].xpath('./text()').extract()
            res.append(item)
        # print res
        return res

    def _process_request(self, request):
        info('process ' + str(request))
        return request
