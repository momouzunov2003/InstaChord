from requests import post,get
import json
import base64

client_id = "7036a820bf15467492ae929f2f064efa"
client_secret = "7d44fd435fe54739bee8c4d205b2ae4b"

def get_token():
    auth_string = client_id +':'+ client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist_id(token, text_input):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={text_input}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items'][0]['id']
    return json_result

def get_artist_top_tracks(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=BG"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    result_array = []
    for idx,song in enumerate(json_result):
        result_array.append(f"{idx+1}. {song['name']}")
    return result_array
    


token = get_token()