import time
from auth import Auth
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#initialize GPIO Mode = BCM
GPIO.setmode(GPIO.BCM)

auth = Auth()
db = auth.get_database()

delay = 1 #delay update for 1s

class IO_Dictionary(dict):
    class NADict(object):
        def __getitem__(self, k):
            return "N/A"
    NA = NADict()
    def __missing__(self, k):
        return self.NA

def stream_handler(gpio) :
    d = IO_Dictionary(gpio["data"])
    dm0 = int(d["GPIO0"]["MODE"])
    dm1 = int(d["GPIO1"]["MODE"])
    dm2 = int(d["GPIO2"]["MODE"])

    dv0 = int(d["GPIO0"]["VALUE"])
    dv1 = int(d["GPIO1"]["VALUE"])
    dv2 = int(d["GPIO2"]["VALUE"])

    # print(dm0,dv0)
    GPIO.setup(17,dm0)
    GPIO.setup(18,dm1)
    GPIO.setup(27,dm2)

    GPIO.output(17,dv0)
    GPIO.output(18,dv1)
    GPIO.output(27,dv2)


ioconf = db.stream(stream_handler)
time.sleep(300)
ioconf.close()
    
    
    # dm1 = int(ioconf["BOARD1"]["MODE"])
    # dv1 = int(ioconf["BOARD1"]["VALUE"])

    #setup
    # GPIO.setup(17,int(dm0))
    # GPIO.setup(18,dm1)

    #output value
    # GPIO.output(17,int(dv0))
    # GPIO.output(18,dv1)






"""
MODE BCM
GPIO.0 = 17
GPIO.1 = 18
GPIO.2 = 27
GPIO.3 = 22
GPIO.4 = 23
GPIO.5 = 24
GPIO.6 = 25
GPIO.7 = 4

SETUP :
GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel, GPIO.OUT)

To read the value of a GPIO pin:
GPIO.input(channel)
(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)). This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

o set the output state of a GPIO pin:
GPIO.output(channel, state)
(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)).
State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

"""
""" =======================wiring pi diagram =================================
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+


"""