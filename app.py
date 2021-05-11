from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

location = input("Enter a location: ")

# def main():
#     getLocation(location)
#     calc()

def getLocation(location):
    loc = Nominatim(user_agent="getLoc")
    getLoc = loc.geocode(location)
    long = getLoc.longitude
    #print(long)
    return long

def calc():
    long = getLocation(location)
    min = long / 0.25
    exactTime = datetime.utcnow() + timedelta(minutes=min)
    print(exactTime)


calc()