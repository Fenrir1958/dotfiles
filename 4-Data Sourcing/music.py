# music.py

# [...] imports
import requests

def fetch_lyrics(artists, title):
    # [...] the body from previous slide
    url = f'https://lyrics.lewagon.ai/search?artist={artists}&title={title}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'NO LYRICS'
    data = response.json()
    return data['lyrics']
