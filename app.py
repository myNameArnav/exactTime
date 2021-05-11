from datetime import datetime, timedelta, timezone, tzinfo
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

location = input("Enter a location: ")

tzf = TimezoneFinder()

def main():
    calc()

def getLocation(location):
    loc = Nominatim(user_agent="getLoc")
    getLoc = loc.geocode(location)
    long = getLoc.longitude
    lati = getLoc.latitude
    return long, lati

def timeZone():
    long, lati = getLocation(location)
    timezone = tzf.timezone_at(lng=long, lat=lati)
    tz = pytz.timezone(timezone)
    return tz

def calc():
    long, lati = getLocation(location)
    tz = timeZone()
    min = long / 0.25
    exactTime = datetime.utcnow() + timedelta(minutes=min)
    currentTime = datetime.now(tz).replace(tzinfo=None)
    
    print("Time Zone:", tz)
    print("\nThe exact time is: " ,exactTime)
    print("The actual time is: ", currentTime, "\n")
    
    delta = exactTime - currentTime
    print("The diffrence is:", delta)


main()