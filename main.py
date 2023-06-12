import os

CONTROL_HEADER = b'\x8C'
QUERY_HEADER = b'\x83'

CATEGORY = b'\x00'
QUERY_DATA = b'\xff\xff'

class Power:
    Code = b'\x00'
    Control = True
    Query = True
    Off = b'\x00'
    On = b'\x01'

class Standby:
    Code = b'\x01'
    Control = True
    Query = False
    Disable = b'\x00'
    Enable = b'\x01'

class Input_Select:
    Code = b'\x02'
    Control = True
    Query = True
    Toggle= b'\x00'
    Video_SCART= b'\x02'
    Component= b'\x03'
    Hdmi= b'\x04'
    Pc= b'\x05'
    Shared_Input= b'\x07'
    N1 	 = b'\x01'	
    N2 	 = b'\x02'	
    N3 	 = b'\x03'	
    N4 	 = b'\x04'	
    N5  = b'\x05'

class Volume_Control:
    Code = b'\x05'
    Control = True
    Query = True
    Up_Down = b'\x00'
    Direct = b'\x01'
    Up 	 = b'\x00'	
    Down 	 = b'\x01'	
    def Direct(value):
        return Direct + value

class Muting:
    Code = b'\x06'
    Control = True
    Query = True
    Toggle = b'\x00'
    Direct = b'\x01'
    Unmuting = b'\x00'	
    Muting = b'\x01'	

class Language:
    Code = b'\x07'

class Off_Timer:
    Code = b'\x0C'
    Control = True
    Query = False
    Toggle = b'\x00'
    Direct = b'\x01'
    def Direct(value):
        return Direct + value

class Picture_Off:
    Code = b'\x0D'
    Control = True
    Query = False
    Toggle = b'\x00'
    Direct = b'\x01'
    Off = b'\x00'
    On = b'\x01'

class Display:
    Code = b'\x0F'
    Control = True
    Query = False
    Toggle = b'\x00'


class Control_Response:
    RESPONSE_HEADER = b'\x70'
    sucess =	b'\x00' # Completed (Normal End)
    overflow =	b'\x01' # Limit Over (Abnormal End – over maximum value) The packet is received normally, but the data value exceeds the upper limit.
    underflow =	b'\x02' # Limit Over (Abnormal End – under minimum value) The packet is received normally, but the data value exceeds the lower limit.
    canceled =	b'\x03' # The packet is received normally, but either the data is incorrect or the request is not acceptable in the current host value.
    parse_error =	b'\x04' # The packet is not received properly (undefined data format) or there is a Check Sum error. However, it will be returned as “Limit over” (0x01 or 0x02) in that case.

def calc_checksum(data):
    sum = 0
    for b in data: 
        sum += int.from_bytes(b, byteorder='big')
    sum = sum % 256
    return chr(sum)

def control_req(function, data):
    length = len(data) + 1
    result = CONTROL_HEADER + CATEGORY + function + length + data
    checksum = calc_checksum(result)
    result = result + checksum
    return result

def query_req(function):
    result = QUERY_HEADER + CATEGORY + function + QUERY_DATA
    checksum = calc_checksum(result)
    result = result + checksum
    return result

def ctl_power():

    control_req(function, data)

# data = "xxxxxxxxxxxxxxxx"
# dev = os.open("/dev/ttyUSB0", os.O_RDWR)
# os.write(dev,data)
# os.lseek(dev,0,os.SEEK_SET)
# print os.read(dev,16)



