from speak import speak
from speak import takecommand
from speak import wishme
import threading

def user_reply():
    takecommand()

if __name__=="__main__":
    wishme()
    while True:
        t1 = threading.Thread(target=user_reply(),args=(10,))
        t1.start()
        t1.join()