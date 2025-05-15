import requests

url = "https://www.instagram.com/api/v1/media/3552562460924492100/comments/?can_support_threading=true&permalink_enabled=false"

headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Csrftoken": "uUJ9TwjX4L6rtGO5obFOvXRC4teLty66",
    "X-Ig-App-Id": "936619743392459",
    "X-Asbd-Id": "359341",
    "X-Ig-Www-Claim": "hmac.AR0GbGu5LJQQqyHNiQdD2NQvR4-EL_XGvP_3dYy0WPJ2yjl9",
    "X-Web-Session-Id": "s7u1c9:vec894:3f9j01",
    "X-Requested-With": "XMLHttpRequest",
    "Dnt": "1",
    "Referer": "https://www.instagram.com/reel/DFNPLxlyrlE/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "Priority": "u=0",
    "Te": "trailers"
}

cookies = {
    "ps_n": "1",
    "ps_l": "1",
    "sessionid": "5467753552:gYPDZKKkQ2wgjh:27:AYf9PifVhFBxddluBKhmeGO7BWJ2iWmQzMR2jge5EQ0",
    "ig_did": "BE946926-76B7-450D-9B4B-E000328BA36D",
    "ds_user_id": "5467753552",
    "csrftoken": "uUJ9TwjX4L6rtGO5obFOvXRC4teLty66",
    "mid": "Zy5FeAAEAAFgul88D4N43Zr4spgE",
    "datr": "FaGCZ5G44cUCgEUwg6OVda3r",
    "wd": "1920x955",
    "rur": "PRN\\0545467753552\\0541778788548:01f7a017bc9f443c887cdb92d902dd4d31061358f785db61b8716e1264f92dd8219c1289"
}

response = requests.get(url, headers=headers, cookies=cookies)

import json
# Check if request was successful
if response.status_code == 200:
    data = response.json()

    with open('reel_comments.json', 'w') as f:
        json.dump(data, f, indent=4)
