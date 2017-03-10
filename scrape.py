from bs4 import BeautifulSoup
import urllib2
import re

url = "https://www.stanfordesp.org/learn/Splash/2009_Fall/catalog"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

# print soup.prettify()

class_list = soup.find_all("div", class_="show_class")
# print classes[0].prettify()

classes = {}
for element in class_list:
    classes[element['id']] = {}

# raw_text = class_list[0].find("div", {"class" : "class_content"}).get_text()
# text = " ".join(raw_text.split())
# print text

# pattern = re.compile("Section .: (\d+) \(max (\d+)\)")
# print type(class_list[0])
# print pattern.match(content).group()


for element in class_list:
    raw_text = element.find("div", {"class" : "class_title"}).get_text()
    text = " ".join(raw_text.split())
    classes[element['id']]["class_title"] = text

    raw_text = element.find("div", {"class" : "class_content"}).get_text()
    text = " ".join(raw_text.split())
    classes[element['id']]["class_content"] = text

print classes
