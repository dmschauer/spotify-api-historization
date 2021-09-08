import json
import os
import time
import datetime

from spotifyclient import SpotifyClient

def main():
    # credentials supplied in environment variables before startup
    # from Dockerfile
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    # from docker-compose.yml
    ARTIST_NAME = os.getenv("ARTIST_NAME")
    INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS"))

    # Spotify Web API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # credentials supplied in environment variables before startup
    spotify_client = SpotifyClient(CLIENT_ID,
                                CLIENT_SECRET,
                                BASE_URL,
                                AUTH_URL)

    # get Spotify ID of artist of interest
    artist_id = spotify_client.get_artist_id_from_search(ARTIST_NAME)

    print("Will process artist {} (Spotiy ID: {}) every {} seconds".format(
        ARTIST_NAME, 
        artist_id, 
        INTERVAL_SECONDS))

    # Periodically load and write data   
    while(True):
        ts = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        print("{}: Processing".format(ts))
        
        top_tracks = spotify_client.get_top_tracks(artist_id)
        
        # write dict as JSON
        filename = 'top_tracks_' + ARTIST_NAME.replace(" ","_") + "_" + ts + '.json'
        with open('/json_data_mount/' + filename, 'w') as file:
            file.write(json.dumps(top_tracks)) 
            # json.dump(top_tracks, file) would work as well but I find above syntax more explicit

        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()