from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

location = input("Enter a location (It can be a city, a state or even a zip code): ")

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
    actualTime = datetime.now(tz).replace(tzinfo=None)

    print("Time Zone:", tz)
    print("\nThe exact time is: ", exactTime)
    print("The actual time is: ", actualTime, "\n")

    if exactTime > actualTime:
        delta = exactTime - actualTime
        sign = "+"
    else:
        delta = actualTime - exactTime
        sign = "-"

    print("The difference is: ", sign, delta)


main()
