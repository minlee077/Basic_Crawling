import urllib.request
import bs4


# html object creation
html = urllib.request.urlopen("https://terms.naver.com/list.nhn?cid=51007&categoryId=51007")

#Beautiful soup
bsObj = bs4.BeautifulSoup(html,"html.parser")

firstDiseaseBlock = bsObj.find("div",{"class":"info_area"}) #crawling based on tag and class name
