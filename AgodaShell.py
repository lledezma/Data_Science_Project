import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlTripadvisor = 'https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF9qc6iYHx6nN7nnGV8SeY3o1vfv%2FfnGBWznj2In3R6GWoHxCNHZ7i%2BMFciATRgDLpWV56jswVWDVKt7cQkuIMT5FhNo5BqKfuIIZg6OdfnBiHUYzT5KXLdOHxeTRZP1x2IKUZZOw71sX%2Fi2VTdi26kgqjOxgX8WMXWZ%2BH845BUS%2BdKT8zx5W5BioMdUuG%2F%2Fqg0mDkh6fdJUSXTb6S93IA7s%3D&city=17072&tick=636213686438&pagetypeid=1&origin=US&cid=-1&tag=&gclid=&aid=130243&userId=654cfbdd-8da6-4313-baf0-cd880efd51af&languageId=1&sessionId=1uxojcjeh30352uqw5rug3rf&storefrontId=3&currencyCode=USD&htmlLanguage=en-us&trafficType=&cultureInfoName=en-US&checkIn=2017-02-08&checkOut=2017-02-09&los=1&rooms=1&adults=2&children=0&priceCur=USD&hotelReviewScore=5&ckuid=654cfbdd-8da6-4313-baf0-cd880efd51af'
pageTripadvisor = requests.get(urlTripadvisor)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupTripadvisor = BeautifulSoup(pageTripadvisor.content, 'lxml')


position = soupTripadvisor.find('section', class_='hotel-item-box')
hotelname = position.find('h3', class_='hotel-name').string
hotelrating = position.find('strong', class_='review-score-label').string

currency = position.find('span', class_='currency dark-gray2').string
hotelprice = currency + '' + position.find('span', class_='price dark-gray1',).string

hoteladdress = position.find('span', class_='areacity-name').find('span').string
hotelreviews = position.find('span', class_='review-count').string




print('Name:', hotelname)
print('Address:',hoteladdress)
print('Price:',hotelprice)
print('Rating:',hotelrating)
print('Reviews:',hotelreviews)