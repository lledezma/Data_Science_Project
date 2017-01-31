import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlHotels = 'https://www.hotels.com/search.do?resolved-location=CITY%3A1504033%3AUNKNOWN%3AUNKNOWN&destination-id=1504033&q-destination=Las%20Vegas,%20Nevada,%20United%20States%20of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=DISTANCE_FROM_LANDMARK'
pageHotels = requests.get(urlHotels)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupHotels = BeautifulSoup(pageHotels.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for position in soupHotels.find_all('article'):
    hotelname = position.find('h3', class_='p-name').find('a').string
    hoteladdress = position.find('div', class_='contact').find('span', class_='p-street-address').string
    hotelcity = position.find('span', class_='p-locality').string
    hotelstate = position.find('span', class_='p-region').string
    hotelpostalcode = position.find('span', class_='p-postal-code').string
    rating = soupHotels.find('span', class_='guest-rating-value').find('strong').string
    try:
        hotelprice = position.find('div', class_='price').find('ins').string
    except AttributeError:
        hotelprice = position.find('div', class_='price').find('b').string

    # Make changes to response for APNewsBriefs
    response.append({'Hotelname': hotelname,
                     'Hoteladdress': hoteladdress, 'Hotelcity': hotelcity,
                    'Hotelstate': hotelstate, 'Hotelpostalcode': hotelpostalcode,
                     'Hotelprice': hotelprice})

# Write response to JSON file
postingsFile = today + '.Hotels.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()