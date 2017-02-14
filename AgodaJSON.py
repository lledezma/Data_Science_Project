import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []


urlAgoda = 'https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF9qc6iYHx6nN7nnGV8SeY3o1vfv%2FfnGBWznj2In3R6GWoHxCNHZ7i%2BMFciATRgDLpWV56jswVWDVKt7cQkuIMT5FhNo5BqKfuIIZg6OdfnBiHUYzT5KXLdOHxeTRZP1x2IKUZZOw71sX%2Fi2VTdi26kgqjOxgX8WMXWZ%2BH845BUS%2BdKT8zx5W5BioMdUuG%2F%2Fqg0mDkh6fdJUSXTb6S93IA7s%3D&city=17072&tick=636213686438&pagetypeid=1&origin=US&cid=-1&tag=&gclid=&aid=130243&userId=654cfbdd-8da6-4313-baf0-cd880efd51af&languageId=1&sessionId=1uxojcjeh30352uqw5rug3rf&storefrontId=3&currencyCode=USD&htmlLanguage=en-us&trafficType=&cultureInfoName=en-US&checkIn=2017-02-08&checkOut=2017-02-09&los=1&rooms=1&adults=2&children=0&priceCur=USD&hotelReviewScore=5&ckuid=654cfbdd-8da6-4313-baf0-cd880efd51af'

parse = True
i = 1


# Parse YouTube url
while parse == True:



    pageAgoda = requests.get(urlAgoda)


    soupAgoda = BeautifulSoup(pageAgoda.content, 'lxml')


for position in soupAgoda.find_all('section', class_='hotel-item-box'):
    hotelname = position.find('h3', class_='hotel-name').string
    hotelrating = position.find('strong', class_='review-score-label').string

    currency = position.find('span', class_='currency dark-gray2').string
    hotelprice = currency + '' + position.find('span', class_='price dark-gray1', ).string

    hoteladdress = position.find('span', class_='areacity-name').find('span').string

    response.append({'Hotelname': hotelname,
                     'Hoteladdress': hoteladdress,
                     'Hotelprice': hotelprice,
                     'Hotelrating': hotelrating})

    parse = False
    for nextPosition in soupAgoda.find_all('span', class_='page-of'):
        if nextPosition.string == 'Page 6 of 1':
            url = 'https://www.agoda.com/' + nextPosition.get('href')
            parse = True
            i += 1
            # print(i)


postingsFile = today + '.Agoda.json'



with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()

