from pySerialTest import serial_stream
from pcLib import cal_expected_number


stream = serial_stream(b'83848690919294')
totalNum = stream.serial_stream_count()


totalFked = 0

poppedElement = stream.serial_stream_pop()

for x in range(0, totalNum-2, 2):
    expectedElement = cal_expected_number(poppedElement)
    poppedElement = stream.serial_stream_pop()

    if (poppedElement != expectedElement):
        totalFked += 1


print(totalFked)
