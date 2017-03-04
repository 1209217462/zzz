# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re
from urllib.parse import  urljoin




#html解析器
class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        #找到形如  view/123.htm 的链接
        links=soup.find_all('a',href=re.compile(r"/view/\d+.htm"))
        for link in links:
            new_url=link["href"]
            #将形如 view/123.html 的链接匹配 page_url的格式改成完整链接，page_url归根结底是页面中的链接
            new_full_url=urljoin(page_url,new_url)
            #将完整链接返回
            new_urls.add(new_full_url) 
        return new_urls
              
    
    def _get_new_data(self, page_url, soup):
        res_data={}
        
        #url
        res_data["url"]=page_url
        
        
        #解析出标题
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"]=title_node.get_text()
        #解析出简介
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find("div",class_="lemma-summary")
        res_data["summary"]=summary_node.get_text()
        
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup=BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data    
        
    
    
    
    

    
    



