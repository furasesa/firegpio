import os
import time
from auth import Auth

auth = Auth()
db = auth.get_database()
print("testing mode")

# Latest Worked
# if 'name' == '__main__':
#     print('from main')
# else:
#     print('calling server_test')
#     io_config = db.get().val()
#     b0 = io_config.get("BOARD0",{}).get("MODE")
#     print(b0)

class IO_Dictionary(dict):
    class NADict(object):
        def __getitem__(self, k):
            return "N/A"
    NA = NADict()
    def __missing__(self, k):
        return self.NA

def stream_handler(gpio) :
    d = IO_Dictionary(gpio["data"])
    dm0 = d["BOARD0"]["MODE"]
    dv0 = d["BOARD0"]["VALUE"]
    print(dm0,dv0)


ioconf = db.stream(stream_handler)
time.sleep(10)
ioconf.close()

# ioconf = IO_Dictionay(db.get().val())
# dm0 = ioconf["BOARD0"]["MODE"]
# dv0 = ioconf["BOARD0"]["VALUE"]
# dm1 = ioconf["BOARD1"]["MODE"]

# print("BOARD0")
# print (dm0,dv0)
