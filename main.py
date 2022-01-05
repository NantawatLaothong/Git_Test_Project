#!/usr/bin/env python

import os
import sys
from download_img import download_image


def main(url, name):
    if not os.path.exists('images'):
        os.mkdir('images')
    download_image(url, name)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

# sample url
# 'https://images-na.ssl-images-amazon.com/images/I/91XPrGekxbL.jpg'
