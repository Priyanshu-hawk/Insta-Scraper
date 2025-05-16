import requests
import re
from config import headers, cookies
from urllib.parse import urlencode, quote_plus
import json

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_user_info(url):
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)

    # Print the response status code

    profile_id = None
    if response.status_code == 200:
        regex = r'"profile_id":\s*"(\d+)"'
        matches = re.findall(regex, response.text)
        if matches:
            profile_id = matches[0]
        else:
            print("Profile ID not found in the response.")

    return profile_id

# def get_

def get_user_reels(profile_id, url, limit=12):
    url = "https://www.instagram.com/graphql/query"

    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Fb-Friendly-Name": "PolarisProfileReelsTabContentQuery",
        "X-Bloks-Version-Id": "446750d9733aca29094b1f0c8494a768d5742385af7ba20c3e67c9afb91391d8",
        "X-Csrftoken": "uUJ9TwjX4L6rtGO5obFOvXRC4teLty66",
        "X-Ig-App-Id": "936619743392459",
        "X-Root-Field-Name": "xdt_api__v1__clips__user__connection_v2",
        "X-Fb-Lsd": "DVG2otd606zWH8rzuN2ybO",
        "Origin": "https://www.instagram.com",
        "Dnt": "1",
        "Referer": "{}/reels".format(url),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "Te": "trailers"
    }

    data_dict = []

    # Initail request

    variables_dict = {
    "data": {
        "include_feed_video": True,  # Python boolean True
        "page_size": 12,
        "target_user_id": str(profile_id)
    }
    }

    other_params = {
        "server_timestamps": True,  # Python boolean True
        "doc_id": "24164713859812789" # Keep as string if it's an ID
    }

    variables_json_string = json.dumps(variables_dict, separators=(',', ':'))

    query_params = {
        "variables": variables_json_string,
        "server_timestamps": str(other_params["server_timestamps"]).lower(), # Convert boolean to lowercase string "true" or "false"
        "doc_id": other_params["doc_id"]
    }

    encoded_data = urlencode(query_params)

    response = requests.post(url, headers=headers, cookies=cookies, data=encoded_data)

    if response.status_code == 200:
        data = json.loads(response.text)

    else:
        print("Error:", response.status_code)
        return data_dict
    
        
    # 2nd request using cursor


# def get_reel

if __name__ == "__main__":
    url = "https://www.instagram.com/sundaysarthak"
    profile_id = get_user_info(url)
    print(f"Profile ID: {profile_id}")
    print(get_user_reels(profile_id, url))