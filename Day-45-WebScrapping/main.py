"""
Main module
"""
from bs4 import BeautifulSoup
import requests

def scrape_ycWebsite():

    response = requests.get("https://news.ycombinator.com/")
    yc_webpage = response.text
    soup = BeautifulSoup(yc_webpage, "html.parser")
    titles = soup.select(".titleline>a")
    title2 = soup.find_all(name="span", class_="score")
    headings = [title.getText() for title in titles]
    links = [title.get("href") for title in titles]
    upvotes = [int(vote.getText().split()[0]) for vote in title2]

    index = upvotes.index(max(upvotes)) # largest index
    print(headings[index])
    print(links[index])

def scrape_100_best_movies():
    """Function extracts 100 best empire movies"""
    url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    resp = requests.get(url)
    web_page = resp.text
    soup = BeautifulSoup(web_page, "html.parser")
    html_title = soup.find_all(name="h3", class_="title")
    titles = [title.getText() for title in html_title]

    with open("movies.txt", "w", encoding="utf-8") as f:
        for title in titles[::-1]:
            f.write(title+"\n")

scrape_100_best_movies()






