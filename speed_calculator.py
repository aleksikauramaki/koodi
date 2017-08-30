from sys import argv

script, time, km = argv

def laske(minutes_seconds, km):
    tmp = minutes_seconds.split(":")
    minutes = int(tmp[0])
    seconds = int(tmp[1])
    minutes = minutes + seconds / 60
    hours = minutes / 60
    km = float(km)
    speed = km / hours
    print("Your average speed was %.2f km/h" % speed)

laske(time, km)