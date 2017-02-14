import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlHotels = 'https://www.hotels.com/search.do?destination-id=1504033&sort-order=DISTANCE_FROM_LANDMARK&q-destination=Las+Vegas,+Nevada,+United+States+of+America&q-room-0-adults=2&pg=1&q-rooms=1&start-index=12&resolved-location=CITY:1504033:UNKNOWN:UNKNOWN&q-room-0-children=0&pn=3'


pageHotels = requests.get(urlHotels)


soupHotels = BeautifulSoup(pageHotels.content, 'lxml')

#position = soupAPNewsBriefs.find('article')
position = soupHotels.find('article')
hotelname = position.find('h3', class_='p-name').find('a').string

addressposition = soupHotels.find('div', class_='contact')
hoteladdress= position.find('div', class_='contact').find('span', class_='p-street-address').string
hotelcity = position.find('span', class_='p-locality').string
hotelstate = position.find('span', class_='p-region').string
hotelpostalcode = position.find('span', class_='p-postal-code').string
rating = soupHotels.find('span', class_='guest-rating-value').find('strong').string
try:
  hotelprice = position.find('div', class_='price').find('ins').string
except AttributeError:
    hotelprice = position.find('div', class_='price').find('b').string
hotelreviews = position.find('div', class_='guest-reviews-link').find('a').string





print('Hotel name: ', hotelname)
print('Address: ', hoteladdress, hotelcity, hotelstate, hotelpostalcode)
print('Rating:',rating)
print('Price:',hotelprice)
print('Reviews:',hotelreviews)




parse = True
i = 1
pageCount = 1



while parse == True:




    # print(url)
    parse = False
    for nextPosition in soupHotels.find_all('div', class_='pagination'):
        if nextPosition.string == "next":
            pageCount += 1
            urlHotels = 'https://www.hotels.com/search.do?destination-id=1504033&sort-order=DISTANCE_FROM_LANDMARK&q-destination=Las+Vegas,+Nevada,+United+States+of+America&q-room-0-adults=2&pg=1&q-rooms=1&start-index=12&resolved-location=CITY:1504033:UNKNOWN:UNKNOWN&q-room-0-children=0&pn=' + str(
                pageCount)
            parse = True
            i += 1
            if pageCount == 6:
                parse = False