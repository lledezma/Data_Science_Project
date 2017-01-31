import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlHotels = 'https://www.hotels.com/search.do?resolved-location=CITY%3A1504033%3AUNKNOWN%3AUNKNOWN&destination-id=1504033&q-destination=Las%20Vegas,%20Nevada,%20United%20States%20of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=DISTANCE_FROM_LANDMARK'
pageHotels = requests.get(urlHotels)

# Prepare for parsing APNewsBriefs with BeautifulSoup
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





print('Hotel name: ', hotelname)
print('Address: ', hoteladdress, hotelcity, hotelstate, hotelpostalcode)
print('Rating',rating)
print(hotelprice)



#print('Hotel Price:', hotelprice)
#print('City', hotelcity)
#print('State', hotelcity, hotelstate)
#print('Zip', hotelpostalco