import json
import requests
from bs4 import BeautifulSoup
url1 = "https://www.googleapis.com/books/v1/volumes?q="

s="Flowers"

fullurl=url1+s
r = requests.get(fullurl)
for count in range(10):
    print(r.json()["items"][count]["volumeInfo"]["title"])
    print("Authors:")
    for i in range(10):
        try:
            print(r.json()["items"][count]["volumeInfo"]["authors"][i])
        except:
            pass
    print("Link:  "+r.json()["items"][count]["volumeInfo"]["previewLink"])    
    try:
        print("Average Rating: ", r.json()["items"][count]["volumeInfo"]["averageRating"])
    except:
        print("No ratings available")
    print()