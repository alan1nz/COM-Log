from collections.abc import Callable, Iterable, Mapping
from typing import Any
import serial
import sched
import time
import threading
from pcLib import cal_expected_number
from threading import Thread
from threading import Timer
import queue


def print_messages():

    while 1:
        LOCK.acquire()
        print("Good", q.get())
        LOCK.release()
        time.sleep(3)


def print_fked_up_messages():

    while 1:
        LOCK.acquire()
        print("fked", q1.get())
        LOCK.release()
        time.sleep(3)


class serial_stream:

    def __init__(self,data):
        self.data = data
        self.startIndex = 0
    def serial_stream_stud(self):
        print(self.data)
        return self.data
    
    def serial_stream_count(self):
        return len(self.data)
    
    def serial_stream_pop(self):
        retValue = self.data[self.startIndex:self.startIndex+2]
        self.startIndex = self.startIndex + 2
        return retValue
        
def read_serial_stream(data):
    COM = "COM5"
    BAUD = 115200
    ser = serial.Serial(COM, baudrate=BAUD, bytesize=8)

    totalMessages = 0
    fkedUpMessages = 0
    expectedByte = b'83'
    previousLine = b'69'
    serialString = data
    # while 1:
    
        # serialString = ser.readline()
    totalMessages += 1

    firstNumber = serialString[0:2]

    if (firstNumber != expectedByte):
        fkedUpMessages += 1
        print("previous line: ", previousLine)
        print("current line: ", serialString)
        print("")

        previousLine = serialString
        expectedByte = cal_expected_number(firstNumber)

        q.queue.clear()  # clear the queue otherwise the next line will raise exception
        q1.queue.clear()
            # Very important to use the nowait verison otherwise the thread will block if the queue is already full
        q.put_nowait(totalMessages)
        q1.put_nowait(fkedUpMessages)


q = queue.Queue()
q1 = queue.Queue()

LOCK = threading.Lock()

t = Thread(target=print_messages)
t2 = Thread(target=print_fked_up_messages)
t3 = Thread(target=read_serial_stream)

# t.start()
# t2.start()
# t3.start()
