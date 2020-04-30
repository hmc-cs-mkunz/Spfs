#Paste these into your UNIX shell before running the program for the first time
#export SPOTIPY_CLIENT_ID="437560379c1a4657aa5cfdf2ef92719d"
#export SPOTIPY_CLIENT_SECRET="e5680ff44c194975a3bba4217c5e2556"
#export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"

import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],)) #my username is mkunz778 (because the app with the id and secret are in my name, it will only work for mine)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_tracks()
for item in results['items']:
    track = item['track']
    print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
