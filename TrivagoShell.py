import requests
from bs4 import BeautifulSoup


urlTrivago = 'http://www.trivago.com/?cpt=3474103&iRoomType=7&aHotelTestClassifier=&iIncludeAll=0&aPartner=&iPathId=34741&aDateRange%5Barr%5D=2017-02-19&aDateRange%5Bdep%5D=2017-02-20&iGeoDistanceItem=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&'
pageTrivago = requests.get(urlTrivago)


soupTrivago = BeautifulSoup(pageTrivago.content, 'lxml')


position = soupTrivago.find('article')
hotelname = position.find('div', class_='item__details').find('span').string

hotelcity = position.find('div', class_='item__details').find('p',class_='details__paragraph').string
hoteladdress= position.find('span', class_='item__distance').string

hotelprice = position.find('div', class_='item__best-details ').find('strong').string
hotelrating = position.find('em', class_='item__rating-number fs-normal').find('span').string


print(hotelname)
print(hotelcity)
print(hoteladdress)
print(hotelprice)
print(hotelrating)


'''
print('Hotel name: ', hotelname)
print('Address: ', hoteladdress, hotelcity, hotelstate, hotelpostalcode)

'''