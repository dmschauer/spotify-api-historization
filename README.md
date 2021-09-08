# What is this?

This is a Docker/Python learning project based on
https://github.com/musikalkemist/spotifyplaylistgenerator 
used for persisting data queried from the Spotify Web API.

You can start up a set up Docker containers based on a single Docker image to persist data about a specific artist of your interest. As a first example it stores the artist's "top tracks" in a shared Docker volume.

I also implemented a second version which uses exactly one Docker container to persist data one or more artists. You can find it here.
#  Build image and run containers
First you have to supply your own Spotify Web API credentials in the ´Dockerfile´. Insert the correct values for ´CLIENT_ID´ and ´CLIENT_SECRET´. Here's a tutorial on how to do so: https://stmorse.github.io/journal/spotify-api.html 

When you're done, run the following command in the root folder of this project: ´docker compose up´

This will create three Docker containers, each storing data in a shared volume every five minutes (unless you supply your own configuration).
# Configuration
In the ´docker-compose.yml´ you find the specification for three Docker containers pre-configured. Here's the code for one of them:
´spotify_python_arctic_monkeys:
    build: .
    environment: 
      - ARTIST_NAME=Arctic Monkeys
      - INTERVAL_SECONDS=300
    volumes:
      - spotify_json:/json_data_mount´

Particularly interesting are the environemnt variables, you might want to change them. They are read in the Python code.

- ´ARTIST_NAME´: Name of the artist you want to store data about. The Python code will first find the Spotify ID of the best-matching artist and subsequently make further API calls to retrieve corresponding data.
- ´INTERVAL_SECONDS´: After retrieving data, wait this many seconds before making the next API call. For example supply 3600 to wait 1 hour.
# Learning resources used / Credits
- Some of the Pyhton code in this project is based on: https://github.com/musikalkemist/spotifyplaylistgenerator

- It's also inspired by this other tutorial on the Spotify API: https://stmorse.github.io/journal/spotify-api.html (mega simple Version)

- General explanation of usage of environment variables in Docker / Compose: https://vsupalov.com/docker-env-vars/

- For future reference about automatically authenticating users: https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/tutorial-reference/Day%2019/notebooks/1%20-%20Auth.ipynb

- I also took a look at the Spotipy library for querying the API but decided against doing to to keep full control over its usage. For other projects it might be helpful: https://spotipy.readthedocs.io/en/2.19.0/