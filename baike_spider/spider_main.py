
from baike_spider import url_manager, html_download, html_parser, html_outputer
class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_download.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
          
    def craw(self, root_url):
        count=1
        #第一个url
        self.urls.add_new_url(root_url)
        #当url管理器还有待爬取URL时
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()             #url列表拿出一个返回url，并标记为已爬取
                html_cont=self.downloader.download(new_url) #获取html页面信息并保持到 html_cont
                print("craw %d : %s"%(count,new_url))       #控制台输出形如   craw 1 : http://baike.baidu.com/item/Python
                new_urls,new_data=self.parser.parse(new_url,html_cont)  #解析  url和内容     
                self.urls.add_new_urls(new_urls)            #将新得到的url列表 加入待爬取url
                self.outputer.collect_data(new_data)        #输出器获取内容信息
                count=count+1   
                #控制爬取页面数量
                if count==300:                              
                    break
            except Exception as e:
                print("craw failed:%s"%e) #打印错误信息
    
        self.outputer.output_html() #输出到文件


if __name__=="__main__":
    root_url="http://baike.baidu.com/item/Python"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)