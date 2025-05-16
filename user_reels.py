import requests
import json
from urllib.parse import urlencode, quote_plus

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
    "Referer": "https://www.instagram.com/ezsnippet/reels",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "Te": "trailers"
}

cookies = {
    "ps_n": "1",
    "ps_l": "1",
    "sessionid": "5467753552%3AgYPDZKKkQ2wgjh%3A27%3AAYc_Jy0r3-4R8Q11VWhQB2FvzObHOPU8ZR_sS6kxULI",
    "ig_did": "BE946926-76B7-450D-9B4B-E000328BA36D",
    "ds_user_id": "5467753552",
    "csrftoken": "uUJ9TwjX4L6rtGO5obFOvXRC4teLty66",
    "mid": "Zy5FeAAEAAFgul88D4N43Zr4spgE",
    "datr": "FaGCZ5G44cUCgEUwg6OVda3r",
    "wd": "1920x955"
}

variables_dict = {
  "data": {
    "include_feed_video": True,  # Python boolean True
    "page_size": 12,
    "target_user_id": "21864547813"
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

# print("Status Code:", response.status_code)

data = json.loads(response.text)

with open("user_reels_1.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data:", data["data"]["xdt_api__v1__clips__user__connection_v2"]["page_info"]["end_cursor"])

variables_dict = {
  "after": data["data"]["xdt_api__v1__clips__user__connection_v2"]["page_info"]["end_cursor"],
  "before": None,
  "data": {
    "include_feed_video": True,
    "page_size": 12,
    "target_user_id": "21864547813"
  },
  "first": 4,
  "last": None
}

other_params = {
    "server_timestamps": True,
    "doc_id": "10087824784583683"
}

variables_json_string = json.dumps(variables_dict, separators=(',', ':'))

query_params = {
    "variables": variables_json_string,
    "server_timestamps": str(other_params["server_timestamps"]).lower(),
    "doc_id": other_params["doc_id"]
}

encoded_data = urlencode(query_params)
response = requests.post(url, headers=headers, cookies=cookies, data=encoded_data)
# print("Status Code:", response.status_code)
data = json.loads(response.text)
with open("user_reels_2.json", "w") as f:
    json.dump(data, f, indent=4)

variables_dict = {
    "after": data["data"]["xdt_api__v1__clips__user__connection_v2"]["page_info"]["end_cursor"],
    "before": None,
    "data": {
        "include_feed_video": True,
        "page_size": 12,
        "target_user_id": "21864547813"
    },
    "first": 4,
    "last": None
}
other_params = {
    "server_timestamps": True,
    "doc_id": "10087824784583683"
}

variables_json_string = json.dumps(variables_dict, separators=(',', ':'))
query_params = {
    "variables": variables_json_string,
    "server_timestamps": str(other_params["server_timestamps"]).lower(),
    "doc_id": other_params["doc_id"]
}
encoded_data = urlencode(query_params)
response = requests.post(url, headers=headers, cookies=cookies, data=encoded_data)

# print("Status Code:", response.status_code)
data = json.loads(response.text)
with open("user_reels_3.json", "w") as f:
    json.dump(data, f, indent=4)