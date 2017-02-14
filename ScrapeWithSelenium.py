from selenium import webdriver
import datetime

today = str(datetime.datetime.now().date())

sites = {'Hotels': 'https://www.hotels.com/search.do?resolved-location=CITY%3A1504033%3AUNKNOWN%3AUNKNOWN&destination-id=1504033&q-destination=Las%20Vegas,%20Nevada,%20United%20States%20of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=DISTANCE_FROM_LANDMARK',
         'Trivago': 'http://www.trivago.com/?cpt=3474103&iRoomType=7&aHotelTestClassifier=&iIncludeAll=0&aPartner=&iPathId=34741&aDateRange%5Barr%5D=2017-02-19&aDateRange%5Bdep%5D=2017-02-20&iGeoDistanceItem=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&',
         'Agoda': 'https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF9qc6iYHx6nN7nnGV8SeY3o1vfv%2FfnGBWznj2In3R6GWoHxCNHZ7i%2BMFciATRgDLpWV56jswVWDVKt7cQkuIMT5FhNo5BqKfuIIZg6OdfnBiHUYzT5KXLdOHxeTRZP1x2IKUZZOw71sX%2Fi2VTdi26kgqjOxgX8WMXWZ%2BH845BUS%2BdKT8zx5W5BioMdUuG%2F%2Fqg0mDkh6fdJUSXTb6S93IA7s%3D&city=17072&tick=636213686438&pagetypeid=1&origin=US&cid=-1&tag=&gclid=&aid=130243&userId=654cfbdd-8da6-4313-baf0-cd880efd51af&languageId=1&sessionId=1uxojcjeh30352uqw5rug3rf&storefrontId=3&currencyCode=USD&htmlLanguage=en-us&trafficType=&cultureInfoName=en-US&checkIn=2017-02-08&checkOut=2017-02-09&los=1&rooms=1&adults=2&children=0&priceCur=USD&hotelReviewScore=5&ckuid=654cfbdd-8da6-4313-baf0-cd880efd51af'
         }

browser = webdriver.Chrome()

for name, link in sites.items():
    response = browser.get(link)
    html = browser.page_source

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, 'w')
    outfile.write(html)
    outfile.close()

#browser.quit()