# Uses the Client Credential flow for authentication.
# This prevents us from seeing private data like hidden user_playlists
# But that is relatively unimportant

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from simplefuse import Passthrough
from fuse import FUSE, FuseOSError, Operations

client_credentials_manager = SpotifyClientCredentials(client_id='437560379c1a4657aa5cfdf2ef92719d', client_secret='e5680ff44c194975a3bba4217c5e2556')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('mkunz778')

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

def main(mountpoint, root):
    FUSE(Passthrough(root), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    main(sys.argv[2], sys.argv[1])
