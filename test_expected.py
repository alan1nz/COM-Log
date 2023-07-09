from pcLib import cal_expected_number
from pySerialTest import serial_stream


class TestClass1:
    def test_answer(self):
        assert cal_expected_number(b"63") == b"64"

    def test_answer1(self):
        assert cal_expected_number(b"99") == b"83"

    def test_answer2(self):
        assert cal_expected_number(b"77") == b"78"

    def test_answer3(self):
        assert cal_expected_number(b"69") == b"70"

    def test_answer4(self):
        assert cal_expected_number(b"85") == b"86"

    def test_answer5(self):
        assert cal_expected_number(b"89") == b"90"


class TestClass2:
    def test_answer(self):
        stream = serial_stream(b"89909192")
        assert stream.serial_stream_stud() == b"89909192"
        # stream.serial_stream_stud(data=b'8990')

    def test_counting_total(self):
        stream = serial_stream(b"89909192")
        assert stream.serial_stream_count() == 4

    def test_counting_total1(self):
        stream = serial_stream(b"838485868788899091929394")
        assert stream.serial_stream_count() == 12

    def test_pop_element1(self):
        stream = serial_stream(b"83848690")

        poppedData = stream.serial_stream_pop()
        assert poppedData == b"83"

        poppedData = stream.serial_stream_pop()
        assert poppedData == b"84"

        poppedData = stream.serial_stream_pop()
        assert poppedData == b"86"

        poppedData = stream.serial_stream_pop()
        assert poppedData == b"90"

    def test_count_fked_up(self):
        stream = serial_stream(b"83848690")


class TestClass3:
    def test_integrated(self):
        stream = serial_stream(b"8384869091")
        totalNum = stream.serial_stream_count()
        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 2

    def test_integrated1(self):
        stream = serial_stream(b"848586878889909192")
        totalNum = stream.serial_stream_count()
        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 0

    def test_integrated1(self):
        stream = serial_stream(b"848586878889909192")
        totalNum = stream.serial_stream_count()

        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 0


    def test_integrated2(self):
        stream = serial_stream(b"90919293949596979899")
        totalNum = stream.serial_stream_count()

        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 0


    def test_integrated3(self):
        stream = serial_stream(b"8399")
        totalNum = stream.serial_stream_count()

        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 1


    def test_integrated3(self):
        stream = serial_stream(b"8485868890")
        totalNum = stream.serial_stream_count()

        totalFked = 0

        poppedElement = stream.serial_stream_pop()

        for x in range(0, totalNum - 2, 2):
            expectedElement = cal_expected_number(poppedElement)
            poppedElement = stream.serial_stream_pop()

            if poppedElement != expectedElement:
                totalFked += 1

        assert totalFked == 2


