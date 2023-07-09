from pcLib import  cal_expected_number
from pySerialTest import serial_stream

class TestClass1:
    def test_answer(self):
        assert cal_expected_number(b'63') == b'64';

    def test_answer1(self):
        assert cal_expected_number(b'99') == b'83';

    def test_answer2(self):
        assert cal_expected_number(b'77') == b'78';

    def test_answer3(self):
        assert cal_expected_number(b'69') == b'70';

    def test_answer4(self):
        assert cal_expected_number(b'85') == b'86';

    def test_answer5(self):
        assert cal_expected_number(b'89') == b'90';


class TestClass2:
    def test_answer(self):
        stream = serial_stream(b'89909192')
        assert stream.serial_stream_stud() == b'89909192'
        # stream.serial_stream_stud(data=b'8990')

    def test_counting_total(self):
        stream = serial_stream(b'89909192')
        