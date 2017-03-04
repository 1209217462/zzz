# -*- coding:utf-8 -*-
from idlelib.iomenu import encoding

 
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    #收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        

    #写入文件中
    def output_html(self):
        fout=open('output.html','w',encoding="utf-16") #使用utf-8时显示 乱码    锛堣嫳
        fout.write("<html>")
        
        fout.write("<body>")
        fout.write("<table border='1'>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data["url"])
            fout.write("<td>%s</td>"%data["title"])
            fout.write("<td>%s</td>"%data["summary"])
            fout.write("</tr>")
            
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    



