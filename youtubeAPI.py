from requests import post,get
import json

api_key = 'AIzaSyDjQV2jwVy8F_Fwfx_7zATKnUNdSgtn5Nc'
def get_youtube_link(song_name):
    url = 'https://www.googleapis.com/youtube/v3/search'
    part = 'snippet'
    type_ = 'video'
    query = f"{url}?key={api_key}&q={song_name}&type={type_}&part={part}"

    result = get(query)
    json_result = json.loads(result.content)
    id = json_result['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v=${id}"
