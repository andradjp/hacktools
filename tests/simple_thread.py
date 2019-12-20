import threading
from time import sleep
from random import randint

class MyThread(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message


    def run(self):
        for x in range(1000):
            print(self.message)
            sleep(0.1)

threads = []
for number in range(0, 5):
    thread = MyThread("I'm the {} thread".format(number))
    thread.name = number
    thread.start()