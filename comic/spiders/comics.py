# -*- coding: utf-8 -*-
import scrapy
from comic.items import ComicItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ComicsSpider(CrawlSpider):
    name = 'comics'
    allowed_domains = ['tw.manhuagui.com']
    start_urls = ['https://tw.manhuagui.com/list/aiqing']
    rules = [
        Rule(LinkExtractor(allow=('^https://tw.manhuagui.com/list/aiqing/index_p([0-9]|[1-1][0-1]).html$')),callback='parse_link',follow='True')
    ]
    # http_user = 'someuser'
    # http_pass = 'somepass'

    def parse_link(self, response):
        #print(response.body.decode('u8'))
        node_list = response.xpath("//body/div[@class='w998 mt10 cf']/div/ul/li")
        #//tr/td[@height="30"]/a[@target='_blank']
        #//tr/td[@height="22"]
        #pass
        #items = []

        #//body/div[@class="w998 mt10 cf"]/div/ul/li/a/img/@src 圖片
        #////body/div[@class="w998 mt10 cf"]/div/ul/li/p/a title
        #//body/div[@class="w998 mt10 cf"]/div/ul/li/span 更新於
        #//body/div[@class="w998 mt10 cf"]/div/ul/li/a/spann更新回數
        #//body/div[@class="w998 mt10 cf"]/div/ul/li//p/a/@href 網頁進入url
        #進入後的各細節 //div/ul[@class="detail-list cf"]/li/span/a [0]year [1]region [2]index [3]category [4]author [5]updateto
        #進入後的內容大綱 //div/div/div[@class="book-detail pr fr"]/div/div

        for node in node_list :
            item = ComicItem()

            #imgsrc = node.xpath("./a/img/@src").extract()
            
            item["imgsrc"] =node.xpath("./a/img/@src").extract_first() 

            item['title'] = node.xpath("./p/a/text()").extract_first()
            item['updatetime'] = node.xpath("./span/text()").extract_first()
            item['updateround'] = node.xpath("./a/span/text()").extract_first()
            #item['weburl'] = node.xpath("./p/a/@href")[0].extract()
            weburl = node.xpath("./p/a/@href")[0].extract()
            item['weburl'] = weburl if 'http:' in weburl else ('https://tw.manhuagui.com'+ weburl)
            yield scrapy.Request(url=item['weburl'],meta={'item':item},callback=self.parse_details,dont_filter=False)
            #item['name','author']=[name,author]
            # item['name'] = name
            # item['author'] = author
            #items.append(item)
            #print(name)
            #print(author)
            #item['id']=0
            #item['id']=item['id']+node_list.index(node)
            #yield item
            
        #return items
    def parse_details(self, response):
        div = response.xpath('//div')
        item = response.meta['item']
        #div = div[0]
        item['year']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[0].extract()
        item['region']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[1].extract()
        item['index']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[2].extract()
        item['category']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[3].extract()
        item['author']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[4].extract()
        item['updateto']=div.xpath('./ul[@class="detail-list cf"]/li/span/a/text()')[5].extract()
        item['idea']=div.xpath('./div/div[@class="book-detail pr fr"]/div/div/text()').extract_first()
    #      item['details'] = response.xpath("//div/ul[@class='detail-list cf']/li/span/a").extract_first()
    #      items.append(item)
        yield item
