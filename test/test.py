import requests
from PIL import Image
import binascii
import io
import base64
url = "https://apis.openapi.sk.com/tmap/staticMap?version=1&coordType=WGS84GEO&width=512&height=512&zoom=15&format=JPG&longitude=126.83529138565&latitude=37.5446283608815&markers=126.978155%2C37.566371_126.108155%2C37.566371"

headers = {
    "accept": "application/json",
    "appKey": "e8wHh2tya84M88aReEpXCa5XTQf3xgo01aZG39k5"
}

response = requests.get(url, headers=headers,stream=True)
if response.status_code == 200:
    with open('test.jpg','wb') as f:
        for chunk in response.iter_content(1024):
                f.write(chunk)
