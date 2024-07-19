# from Function.speak import speak
from speak import takecommand
from speak import wishme
import threading
from Battery import Control

def user_reply():
    takecommand()

def read_question_send_to():
    read = open('C:\\Users\\snaku\\OneDrive\\Desktop\\python\\Advanced_Jarvis\\Txt\\Question.txt','r')
    console = read.read()
    print(console)

            
if __name__=="__main__":
    wishme()
    while True:
        t1 = threading.Thread(target=user_reply(),args=(10,))
        t2 = threading.Thread(target=Control.advice(),args=(10,))


        t1.start()
        t2.start()
        t1.join()
        t2.join()