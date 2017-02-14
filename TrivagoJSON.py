import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

page = 0

for x in range(0,15):
    print(page)
    if(page==200):
        break
    urlTrivago = 'http://www.trivago.com/?iPathId=34741&bDispMoreFilter=false&aDateRange%5Barr%5D=2017-02-19&aDateRange%5Bdep%5D=2017-02-20&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&iRoomType=7&sOrderBy=relevance%20desc&aPartner=&aOverallLiking=1%2C2%2C3%2C4%2C5&iOffset='+str(page)+'&iLimit=25'
    pageTrivago = requests.get(urlTrivago)
    soupTrivago = BeautifulSoup(pageTrivago.content, 'lxml')

    page += 25

    for position in soupTrivago.find_all('article'):
        hotelname = position.find('div', class_='item__details').find('span').string
        hotelcity = position.find('div', class_='item__details').find('p').string
        hoteladdress = position.find('span', class_='item__distance').string
        hotelprice = position.find('div', class_='item__best-details ').find('strong').string
        try:
            hotelrating = position.find('span', class_='rating-number__value').string
        except AttributeError:
            hotelrating = 'none'
        try:
            hotelreviews = position.find('span', class_='review__count').string
        except AttributeError:
            hotelreviews = 'none'

        response.append({'Hotelname': hotelname,
                     'Hotelcity': hotelcity,
                     'Hoteladdress': hoteladdress,
                     'Hotelprice': hotelprice,
                     'Hotelrating': hotelrating,
                     'Hotelreviews': hotelreviews})


postingsFile = today + '.Trivago.json'



with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()