from firebase import firebase
from io_dict import IO_Dictionary

class firetest():
    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://furasesa.firebaseio.com/', None)
        self.result = self.firebase.get('/raspberry', None) #false lint

    def test(self):
        #public mode
        # print ("firebase test result :",end="")
        print (self.result) #test ok
    
    def getdata(self):
        d = IO_Dictionary(self.result)
        return self.result


if __name__ == '__main__':
    # testing
    try:
        mfiretest = firetest()
        # mfiretest.test()
        mfiretest.getdata()
    except Exception as ex:
        print ('firebase test is error :',ex)