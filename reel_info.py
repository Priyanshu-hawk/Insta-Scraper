import requests

url = "https://www.instagram.com//api/v1/media/3552562460924492100/info/"

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
    "Referer": "https://www.instagram.com/reel/DJXKlVOOq-m/",
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
}

response = requests.get(url, headers=headers, cookies=cookies)

import json
# Check if request was successful
if response.status_code == 200:
    data = response.json()

    with open('reel_info.json', 'w') as f:
        json.dump(data, f, indent=4)

else:
    print("Error:", response.status_code)
    print("Response:", response.text)