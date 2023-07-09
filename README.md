# COM-Log

This project is intended for reading the data stream from the serial port and calculates how many times the serial stream
does not match the expected stream.

Example: Given the following data stream b'89 90 91 92 93 94 95 96 97 98 99', the number of times that the stream 
         is screwed up is 0, and the total messages is 11
Example: Given the following data stream b'89 90 92 93 94 95 96 97 98 99', the number of times that the stream is
         screwed up is 1, and the total message is 10, giving 10% loss
Example: Give the following data stream b'89 90 93 94 95 96 97 98 99', the number of times that the stream is screwed
         up is 1, and the total message is 9, giving 11% loss (1/9). But ideally we should get 18% loss (2/11).
