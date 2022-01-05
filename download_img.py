import requests


def download_image(url, name):
    r = requests.get(url)
    with open('images/' + name, 'wb') as f:
        f.write(r.content)
