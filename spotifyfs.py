#Paste these into your UNIX shell one time before running the program
#export SPOTIPY_CLIENT_ID="437560379c1a4657aa5cfdf2ef92719d"
#export SPOTIPY_CLIENT_SECRET="e5680ff44c194975a3bba4217c5e2556"
#export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"



from __future__ import with_statement
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
scope = 'user-library-read'

import os
import sys
import errno

from fuse import FUSE, FuseOSError, Operations
from Passthrough import Passthrough

class Spfs(Passthrough):

    
    def __init__(self, root):
        self.root = root
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


def main(mountpoint, root):
    FUSE(Spfs(root), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    main(sys.argv[3], sys.argv[2])

