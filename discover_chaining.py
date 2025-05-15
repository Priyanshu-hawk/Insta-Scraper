import requests

url = "https://www.instagram.com/graphql/query"

headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Fb-Friendly-Name": "PolarisProfileSuggestedUsersWithPreloadableQuery",
    "X-Bloks-Version-Id": "446750d9733aca29094b1f0c8494a768d5742385af7ba20c3e67c9afb91391d8",
    "X-Csrftoken": "uUJ9TwjX4L6rtGO5obFOvXRC4teLty66",
    "X-Ig-App-Id": "936619743392459",
    "X-Root-Field-Name": "xdt_api__v1__discover__chaining",
    "X-Fb-Lsd": "DVG2otd606zWH8rzuN2ybO",
    "X-Asbd-Id": "359341",
    "Origin": "https://www.instagram.com",
    "Dnt": "1",
    "Referer": "https://www.instagram.com/elementec/reels",
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

data = """av=17841405326583469&__d=www&__user=0&__a=1&__req=7&__hs=20222.HYP%3Ainstagram_web_pkg.2.1...1&dpr=1&__ccg=GOOD&__rev=1022823110&__s=4u0avn%3Aex5txy%3Axr5x4a&__hsi=7504385586928325046&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0DU2wx609vCwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2swtUd8-U2zxe2GewGw9a361qwuEjUlwhEe87q0oa2-azqwt8d-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlA3a3zhA6bwIxeUnAwHxW1oxe6UaU3cyUC4o16UswFw&__csr=gV5jigghAjb6RYbSOOOnQGmZd_FTjtQOQLKHAgAzoyAh9d-ny4CiBChZbVubh8OiEQAPz4AEBa8panzVFGHK9LHHyq-VdaQ8RCDV8D8V99pfl2u9KK4eqAUOV8Fx69Aymt2XnUnKmUKVozryE-icwIzp9VUWXzaK6ucwkE01h-o1FpBg13E4-0JEiVneGx21eg565pU3rwxppQaCg27ouwvdwCKi1uwUypZ0o8460dpw1pi0r-3-44489E4-0kBzP389k2yp584of63909h0Dyk0HE3GwMhFQaDwbygB0cul0b10Nl0iHa0_405381G212fw2kkUy4o06q-08uwcm039y&__hsdp=l0xM_21OEJWEowFMyiiwI499oVdoyW48mNWcb2IkM-z4wzBO1m4uk82XAOJwrNgvx61Uo9Xoox13EEyxK9DF364ogwGhm1ixd8wgwqVE5mi3uq261XwKyUaECUgG8wSw6Zx91S4o0DO0qS0zU6G2u13wlo4pm5E4O585ybwzwwg1eEbWwpUng2Ww_weC3q0gC2ZwrUc8b8_p8&__hblp=0mE4q13xS0S8sweq3S2u7Edo4qaxi2a4XBCwGhmbAG8guy8O2K1dDBz-iawxxi9yp8aXChEy68O1KwKBBCwgGy8oz8gw6KzEgQ7ohwZwEU7a7-0Jo9o2ywa61owba0zU6G2u7E94i1fg88K5TomxO6ryFFUO2-EtDyU8U84E9oao8E34wGAG1DyoR3E2kxq6E99U32xW489o8-2O0JEbS1LwMwIzZAw&__comet_req=7&fb_dtsg=NAftd5lqcs0cyo7PyMI74zRsjjhpGU2SCnl0tb5T8_lb9lsRfDNLedA%3A17843683126168011%3A1729496662&jazoest=26400&lsd=DVG2otd606zWH8rzuN2ybO&__spin_r=1022823110&__spin_b=trunk&__spin_t=1747250926&__crn=comet.igweb.PolarisProfileReelsTabRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisProfileSuggestedUsersWithPreloadableQuery&variables={\"module\":\"profile\",\"target_id\":\"242598499\"}&server_timestamps=true&doc_id=9363787483732960"""

response = requests.post(url, headers=headers, cookies=cookies, data=data)

# print(response.status_code)
import json
data = json.loads(response.text)

with open("discover_chains.json", "w") as f:
    json.dump(data, f, indent=4)
