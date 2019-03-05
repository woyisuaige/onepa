#encoding='utf-8'
#####################################爬电影网一些数据
import requests
from lxml import etree
Url="http://www.1905.com"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:65.0) Gecko/20100101 Firefox/65.0",
"Referer":"http://www.1905.com/mdb/film/newfilm/c0s2.html",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
#333###########################进入详细页面的解析
def get(new_url):#请求网页并解析到详细网页地址
	#url="http://www.1905.com/mdb/film/newfilm/c0s2p1.html"
	response=requests.get(new_url,headers=headers)
	text=response.text
	html=etree.HTML(text)
	#result=etree.tostring(html,encoding="utf-8")
	#print(type(result))
	#print(result.decode("utf-8"))
	#"//ul[@class=\"time-list\"]"
	detail_urls=html.xpath("//div[@class=\"fl pl15 filmInfo\"]/h3/a/@href")
	new_url=(map(lambda detail_urls:Url+detail_urls,detail_urls))#匿名函数以及map函数用法（组装网址）
	return new_url
def exhaustive_movie(x_url):#详细页面中提取想要的数据
	movie={}
	response=requests.get(x_url,headers=headers)
	text=response.text
	x_html=etree.HTML(text)
	min_zi=x_html.xpath("//div[2]/h1/text()")
	min_zi=[i.strip() for i in min_zi if i.strip()!='' ]
	movie["min_zi"]=min_zi
	xing_xins=x_html.xpath("//div[@class='information-list']//text()")
	xing_xins=[i.strip() for i in xing_xins if i.strip()!='' ]#处理列表的空格以及不要的元素
	movie["xing_xins"]=xing_xins
	people=x_html.xpath("//div[@class='creator']//text()")
	people=[i.strip() for i in people if i.strip()!='' ]
	movie["people"]=people
	hai_bao=x_html.xpath("//div//img[@class='poster']/@src")
	movie["hai_bao"]=hai_bao
		#for key in  movie.key():#遍历字典所用项
		#print(movie.values())	
	return movie
def pa_url():#控制爬取网站页码的数量
	url="http://www.1905.com/mdb/film/newfilm/c0s2p{}.html"
	for i in range(1,5):#控制提取页数
		new_url=url.format(i)#指定位置添加元素
		n_urls=get(new_url)
		for x_url in n_urls:
			movie=exhaustive_movie(x_url)
			print(movie)
	return
# for i in movies:
# 	print(movies)
	#movies.append(movie)
#for item in  exhaustive_movie().items():#遍历字典所用项
		#print(item)	
################	电影网数据的提取################################	
pa_url()





