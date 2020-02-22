import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials
SPOTIPY_CLIENT_ID="41ab06391a18471bad7528fa4952ed8d"
os.environ['SPOTIPY_CLIENT_ID'] = '41ab06391a18471bad7528fa4952ed8d'
os.environ["SPOTIPY_CLIENT_SECRET"] = "eff525cb68ee46c8a3623eb627ff00f5"

playlist = "https://api.spotify.com/v1/user/41ab06391a18471bad7528fa4952ed8d/playlists"

# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#
# results= sp.search(q='imagine dragons', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])