import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

page = 0

for x in range(0,25):
    print(page)
    page+=1
    urlHotels = 'https://www.hotels.com/search.do?destination-id=1504033&sort-order=DISTANCE_FROM_LANDMARK&q-destination=Las+Vegas,+Nevada,+United+States+of+America&q-room-0-adults=2&pg=1&q-rooms=1&start-index=12&resolved-location=CITY:1504033:UNKNOWN:UNKNOWN&q-room-0-children=0&pn='+str(page)
    pageHotels = requests.get(urlHotels)
    soupHotels = BeautifulSoup(pageHotels.content, 'lxml')

    for position in soupHotels.find_all('article'):
        hotelname = position.find('h3', class_='p-name').find('a').string

        addressposition = soupHotels.find('div', class_='contact')
        hoteladdress = position.find('div', class_='contact').find('span', class_='p-street-address').string
        hotelcity = position.find('span', class_='p-locality').string
        hotelstate = position.find('span', class_='p-region').string
        hotelpostalcode = position.find('span', class_='p-postal-code').string
        rating = soupHotels.find('span', class_='guest-rating-value').find('strong').string


        try:
            hotelreviews = position.find('div', class_='guest-reviews-link').find('a').string
        except AttributeError:
            hotelreviews = 'none'
        try:
            hotelprice = position.find('div', class_='price').find('ins').string
        except AttributeError:
            hotelprice = 'none'
        try:
            hotelprice_discount = position.find('div', class_='price').find('b').string
        except AttributeError:
            hotelprice_discount = 'none'

        # Make changes to response for APNewsBriefs
        response.append({'Hotelname': hotelname,
                     'Hoteladdress': hoteladdress, 'Hotelcity': hotelcity,
                    'Hotelstate': hotelstate, 'Hotelpostalcode': hotelpostalcode,
                     'Hotelreviews': hotelreviews,'HotelRating': rating,
                      'Hotelprice': hotelprice,'Hotelprice Discount': hotelprice_discount})



postingsFile = today + '.Hotels.json'


with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()