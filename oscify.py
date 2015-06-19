# --------------------------------------------
# harpy
#
# Driver for Human Harp modules. Reads in 
# serial data and outputs OSC messages.
# 
# 
# 
# Becky Stewart of Anti-Alias Labs
# April 2013
# --------------------------------------------

# Returned OSC Message Structure
# /harp/id/hello/value_int32
# /harp/id/angle/angle_id/value_int32
# /harp/id/rotations/value_int32
# /harp/id/speed/value_float32
# /harp/id/acceleration/value_float32

# Send OSC Message Structure
# /toharp/hello/value_int32

from OSC import OSCClient, OSCMessage, OSCServer
import serial
import shlex

client = OSCClient()
client.connect( ("127.0.0.1", 12001) )

# may need to run python -m serial.tools.list_ports
# from the terminal to find correct port name
#ser = serial.Serial("/dev/tty.usbmodem1d11")  
# ser = serial.Serial("/dev/tty.usbmodemfd121")
#ser = serial.Serial("/dev/ttyACM0")
ser = serial.Serial("/dev/tty.usbmodem1421")


# read in next line from serial port and parse
def process_next_line( ):
    line_in = ser.readline().rstrip()
    # print line_in
      
    # serial_dict = dict( [token.split(' ') for token in shlex.split(line_in) if len(token.split(' '))==2] )
    serial_list = line_in.split(' ')
    serial_list  = map(floatify, serial_list)

    print serial_list
    # send OSC
    m = OSCMessage( "/touch")
    m += serial_list
    # print m
    client.send( m )


# try and convert string to float
# if throws an error, just bail
def floatify( old_string ):
    try:
        return float(old_string)
    except:
        pass



def main():    
    try:
        while 1:
            process_next_line()
    except KeyboardInterrupt: 
        ser.close()
        print "Goodbye!"
    

if __name__ == '__main__':
    main()
