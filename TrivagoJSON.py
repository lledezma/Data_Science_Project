import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []


urlTrivago = 'http://www.trivago.com/?cpt=3474103&iRoomType=7&aHotelTestClassifier=&iIncludeAll=0&aPartner=&iPathId=34741&aDateRange%5Barr%5D=2017-02-19&aDateRange%5Bdep%5D=2017-02-20&iGeoDistanceItem=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&'
pageTrivago = requests.get(urlTrivago)


soupTrivago = BeautifulSoup(pageTrivago.content, 'lxml')


for position in soupTrivago.find_all('article'):
    hotelname = position.find('div', class_='item__details').find('span').string
    hotelcity = position.find('div', class_='item__details').find('p').string
    hoteladdress = position.find('span', class_='item__distance').string
    hotelprice = position.find('div', class_='item__best-details ').find('strong').string
    hotelrating = position.find('em', class_='item__rating-number fs-normal').find('span').string


    response.append({'Hotelname': hotelname,
                     'Hotelcity': hotelcity,
                     'Hoteladdress': hoteladdress,
                     'Hotelprice': hotelprice,
                     'Hotelrating': hotelrating})


postingsFile = today + '.Trivago.json'



with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()