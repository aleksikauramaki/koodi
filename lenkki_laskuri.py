class LenkkiLaskuri(object):
    
    def __init__(self, minutes, seconds, km):
        self.minutes = minutes
        self.seconds = seconds
        self.km = km

    def laske(self):
        self.minutes = self.minutes + int(self.seconds) / 60
        hours = self.minutes / 60
        speed = self.km / hours
        print("Your average speed was %.2f km/h" % speed)

temp2 = LenkkiLaskuri(22, 22, 4)

temp2.laske()