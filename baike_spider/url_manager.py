
class UrlManager(object):
    def __init__(self):
        self.new_urls=set() #未爬取url列表
        self.old_urls=set() #已爬取url列表
         
        
    #将新url加入未爬取url列表 
    def add_new_url(self,url):
        if url is None:
            return
        
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        
    #批量将新url加入未爬取url列表
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
            

    #判断是否还有未爬取url
    def has_new_url(self):
        return len(self.new_urls)!=0
   

    #从未爬取url列表中获取url，并将它加入已爬取列表
    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url) #加入已爬取列表
        return new_url   #获取url


    


    
    
    
    
    
    
    
    
    
    



