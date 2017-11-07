import pyrebase
import json
from auth import Auth

#TODO: using class
"""
ex
class Flight(object):

    def __init__(self, duration):
        self.duration = duration


class Airplane(object):

    def __init__(self):
        self.flights = []

    def add_flight(self, duration):
        self.flights.append(Flight(duration))


class Player(object):

    def __init__ (self, stock = 0, bank = 200000, fuel = 0, total_pax = 0):
        self.stock = stock
        self.bank = bank
        self.fuel = fuel
        self.total_pax = total_pax
        self.airplanes = []


    def add_planes(self):
        self.airplanes.append(Airplane())

if __name__ == '__main__':
    player = Player()
    player.add_planes()
    player.airplanes[0].add_flight(5)

"""

# TODO : Rencana :
# 1. calling auth class
# 2. set from json file
# 3. Control
class GPIO_Uplaoder :
    def __init__(self):
        self.mauth = Auth()
        self.mdb = self.mauth.get_database()
        with open("gpio.json") as gpio_conf:
            self.json_data = json.load(gpio_conf) # good
    def execute(self) :
        self.mdb.set(self.json_data)

    # def setchannel(self,channel):
    #     print(self.mdb)
    #     self.ch_sel = self.mdb
    #     self.ch_sel = self.mdb.child(channel)
    #     # print('selected channel',self.ch_sel.get().key())
    #     # return self.ch_sel
    # def addmode(self,value):
    #     self.ch_sel.set({'mode':value})

if __name__ == '__main__':
    uploader = GPIO_Uplaoder()
    uploader.execute() # good
else:
    print(
"""
example :
uploader = GPIO_Uplaoder()
uploader.execute()
""")


# BUG
"""
re-using setchannel
"""



# channel, mode, value = input("channel mode value :").split(" ")
# mdb = mdb.child("gpio").child("raspbian").child(channel)
# try:
#     mdb.set({mode:value})
# except RuntimeError:
#     print("error setting gpio")