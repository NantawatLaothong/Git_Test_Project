import requests

def download_image(url):
    r = requests.get(url)
    with open('images/pic.jpg','wb') as f:
        f.write(r.content)
