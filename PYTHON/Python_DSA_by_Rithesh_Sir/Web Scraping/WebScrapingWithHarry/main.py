
#Install all packages

#step0
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = 'https://codewithharry.com'

#step1: get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step2: Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)


#step3: HTML Tree Traversal

#Commonly used types of Objects
#print(type(title)) #1. Tag
#print(type(title.string)) #2. Navi
#print(type(soup)) #3. BeautifulSoup
#4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
#print(soup2.p)
#print(soup2.p.string)
#print(type(soup2.p.string))
#exit()

#Get the title of the HTML page
title = soup.title
#print(title.string)

#Get the paragraphs from the page
paras = soup.find_all("p")
#print(paras)

#Get the anchors tag from the page
#anchors = soup.find_all("a")
#print(anchors)

#Get first element in the HTML page
#print(soup.find('p'))

#Get classes of any element in the HTML page
#print(soup.find('p')['class'])


#find all the elements with class lead
#print(soup.find_all("p",class_="text-sm"))


#get the text from the tags/soup
#print(soup.find('p').get_text())

#print(soup.get_text())


#Get all the anchors tag from the page
anchors = soup.find_all("a")
all_links = set()
#get all links on the page:

# for link in anchors:
#     print(link.get('href'))


for link in anchors:
    if (link.get('href') != "#"):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(linkText)
        #print(linkText)


# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
navbarSupportedContent = soup.find(id='imgpreview2')
# for element in navbarSupportedContent.contents:
#     print(element)

#stripped_strings we can use in place of strings
# for element in navbarSupportedContent.strings:
#     print(element)

# print(navbarSupportedContent.parent)
# print(navbarSupportedContent.parents)


# for item in navbarSupportedContent.parents:
#     #print(item)
#     print(item.name)


# print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)


ele = soup.select('.text-purple-700')
print(ele)