"""
Main module
"""
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET = os.environ.get('SECRET')

bill_board_base_url = "https://www.billboard.com/charts/hot-100/"
DATE: datetime
# input prompt
def user_date():
    """Checks user input date and return the correct url"""
    global DATE
    time_line= input("Which year do you want to travel to? Enter the date in the format YYYY-MM-DD:")
    try:
        date_obj = datetime.strptime(time_line, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date or date format")
        user_date()
    else:
        DATE = date_obj
        str_date = date_obj.strftime("%Y-%m-%d")
        return bill_board_base_url + str_date + "/"

def scrap_bill_board_songs():
    """Scrapes the bill board web page for the hot 100 songs"""
    resp = requests.get(user_date())
    resp.encoding = "UTF-8"
    bill_board_page = resp.text
    soup = BeautifulSoup(bill_board_page, "html.parser")
    names = soup.select("li.o-chart-results-list__item>h3.c-title")
    #song_names_h3 = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
    song_names = [song.getText().strip('\t\n') for song in names]
    return song_names
def spotify_calls():
    """Interacts with spotify"""
    global DATE
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=CLIENT_ID,
            client_secret=SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    song_names = scrap_bill_board_songs()
    str_date = DATE.strftime("%Y-%m-%d")
    song_uris = []
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{DATE.year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    playlist = sp.user_playlist_create(user=user_id, name=f"{str_date} Billboard 100", public=False)
    # print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

spotify_calls()


