import serial
import time
import sys
from socketIO_client import SocketIO as io


ser = serial.Serial('/dev/cu.usbmodem1411', 115200)

#websocket
OPTS = {
  'path': '/',
}
socket = io('130.211.90.179', 3000, params=OPTS)

def command(msg):
	global serial
	global ser
	print msg
	ser.write(str(unichr(int(msg))))

print ("connected")
socket.on('command', command)
socket.emit('request', '?')
socket.wait(seconds=1000)
##

print (ser)
for _ in range(3):
	print "end of the game"
	socket.emit('command', 'end')
	ser.write(str(unichr(0)))
	time.sleep(0.5)
	ser.write(str(unichr(0+50)))
	time.sleep(0.5)
	ser.write(str(unichr(49)))
	time.sleep(0.5)
	ser.write(str(unichr(49+50)))

ser.close()
