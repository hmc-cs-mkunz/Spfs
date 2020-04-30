# SpFS (Renewed)

This is the original plan but using Spotipy in place of libspotify and fusepy in place of libfuse. 

To get started, make sure you are using a UNIX shell. 

You'll want to run 

```bash
pip install spotipy
```

Once you've installed spotipy, change directories into the Spfs directory and add the following variables to your environment (just copy and paste):

```bash
export SPOTIPY_CLIENT_ID="437560379c1a4657aa5cfdf2ef92719d"
export SPOTIPY_CLIENT_SECRET="e5680ff44c194975a3bba4217c5e2556"
export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"
```

Then you should be able to run the program. I used python3 so I did

```bash
python3 spotifyfs.py mkunz778
```

The argument is my username and the program currently only works with my username but that should suffice for our needs to test functionality. 

Valuable sources I found:

https://github.com/plamere/spotipy

https://thepythoncorner.com/dev/writing-a-fuse-filesystem-in-python/

https://spotipy.readthedocs.io/en/2.12.0/



## Spfs (Original)
  The aim of this project is to build a FUSE file system that acts as an interface for Spotify locally. We want to be able to support logging in to a session, browsing, playback, and SQL queries. Our file system will require an internet connection, as well as a valid Spotify premium subscription. 
  
  Spotify is one of the most popular audio streaming services, and offers a web API as well as a web playback API, accompanied by extensive documentation. The web API allows users to search all songs, artists, or playlists, as well as access user data such as saved tracks and albums. The web playback API will allow us to support music playback. 
  
  We will be using FUSE (Filesystem in Userspace) and C in our implementation. We will be using an existing open-source project called spotifile as a guide for our own. The existing project implements a FUSE file system that creates three directories: browse, playlists, and search. A text file named “connection” is also created and describes the current state of the Spotify connection. The playlists directory is made up of two subdirectories: meta and music. A “ls” command on the meta subdirectory will list your playlists, and the music subdirectory holds .wav files for each track to facilitate playback. Each subdirectory under “meta” contains a collection of symlinks (one representing each track) and points to the corresponding track in the “browse” directory. These symlinks are created lazily meaning they materialize only as something referring to them is inspected by the user. For our implementation of a Spotify interface. We will be initializing two of these three directories upon creation: browse and playlists. The search functionality will be modified to support SQL queries. 
  
  The Spotify data layout (playlists, artists, track names) should be well-suited to SQL queries such that we can write queries such as “name in \playlists\music where name startswith ‘George’” and return results to the user either in a formatted SQL-like table or in an equally organized terminal output. We will implement this using a parser to read the relevant data from the query and doing a filtered search through the specified path. It may be useful to set a limit to the amount of results we return as too wide a query might be detrimental to performance. The Spotifile project that we are using as a backbone has implemented an experimental search directory that is populated asynchronously. 
  
  However, we won’t be populating a directory with our search and instead we will allow users to make SQL-like queries for the file system from the command line. After a connection is confirmed, we can populate a map of track names by adding them upon user inspection (same lazy creation style as Spotifile), and implement functions that will properly return a list of tracks involving the desired query. The map will allow us to make these queries relatively quickly -- we will populate the map by hashing the tracks names against their ASCII representation, and then using this same hash function to find their location later. For now, we imagine we will have to 
cap the number of tracks we save in the map, or whatever data structure seems most appropriate then to assist with the search operation.


Sources: 
https://github.com/upcrob/fsq 
https://github.com/catharsis/spotifile 



