"""
Concepts module
"""
import lxml # for occassions where html.parser is not working
from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title) gets the title including the title tag
# print(soup.title.name) gets the name of the title i.e the title
# print(soup.title.string) gets the string within the title tag e.g Alexa's website
# print(soup.a.string) gets only the first anchor tag in the website
# to get all the achor tags use
# all_a = soup.find_all(name="a")
# for a in all_a:
#     # print(a.getText()) # prints the strings
#     print(a.get("href")) # gets the hrefs used

# to get a specific element use
head = soup.find(name="h1", id="name")
# print(head.getText())
# to get a specific element with a given class
sec_heading = soup.find(name="h3", class_="heading")
# print(sec_heading.getText())
company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
all_headings = soup.select(selector=".heading") # returns a list of all the headings
print(all_headings)