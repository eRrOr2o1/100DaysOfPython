import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Scraping Billboard 100

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date[:4]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")

scraped = [song.getText().strip("\n") for song in soup.find_all(name="h3", class_="c-title", id="title-of-a-story")][5:]

scraped_art = [artist.getText().strip("\n") for artist in soup.find_all(name="span", class_="c-label")]

song_names = [name.replace("'", "").replace("!", "") for name in scraped
              if 'Songwriter(s):' not in name
              if 'Producer(s):' not in name
              if 'Imprint/Promotion Label:' not in name
              if 'Additional Awards' not in name
              ][:100]

artist_names = [artist.split(" Featuring")[0].split(" Duet")[0].replace("Ke$ha", "Kesha") for artist in scraped_art
                if not artist.isnumeric()
                if artist != "-"
                if artist != "NEW"
                if 'ENTRY' not in artist
                ]

# Spotify Authentication
spotify_client_id = "c7e303de427a4221b9499f4ae6aab3a9"
spotify_client_secret = "cf009d743b034d9db47d590ea286632d"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
user_name = sp.current_user()["display_name"]

# Searching Spotify for songs by title
song_urls = []
for song, artist in zip(song_names, artist_names):
    items = sp.search(q=f"track: {song} artist: {artist}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)


