#@brief: this function takes in a byte array and converts it to the next expected
#        byte array by converting the byte array into integer and increment it by 1

#@input: currnentNumber is an byte array ranging from b'83' to b'99'

def cal_expected_number(currentNumber):

    if(currentNumber == b'99'):
        return b'83'
    
    #Because the calculation is done using the decimal representation of the ASCII Char, adding 1 to b'9" returns the
    #ASCII Char ":" so the code below manually converts the second byte into b'0' and increments the first byte by 1
    if(currentNumber[1] == 57):
        # currentNumber[1] == 48
        index0Int = currentNumber[0] +  1
        currentNumber[0] == int.to_bytes(index0Int)
        # retValue[1] = int.to_bytes(index0Int)
        wdf = int.to_bytes(index0Int,length=1,byteorder='big')
        retValue = b'0'
        retValue = wdf + retValue
        return retValue
    
    currentNumberInt = int.from_bytes(currentNumber ,byteorder='big');
    expectedInteger = currentNumberInt + 1;
    expectedByteArray = int.to_bytes(expectedInteger,length=2,byteorder='big');
    return expectedByteArray



