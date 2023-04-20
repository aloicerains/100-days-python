"""Post Module"""
import requests
fake_url = "https://api.npoint.io/11a999948372cffca81c"
class Post:
    def __init__(self):
        self.resp = requests.get(url=fake_url)
        self.resp.raise_for_status()
        self.posts = self.resp.json()
    def get_posts(self):
        return self.posts


