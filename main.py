import os, sys
from download_img import download_image

def main(url):
    if not os.path.exists('images'):
        os.mkdir('images')
    download_image(url)

if __name__ == "__main__":
    main(sys.argv[1])

# 'https://images-na.ssl-images-amazon.com/images/I/91XPrGekxbL.jpg'
