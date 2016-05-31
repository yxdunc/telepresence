import serial
import time
ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
def	move(x, y):
	ser.write(str(unichr(int(x % 49))))
	ser.write(str(unichr(int(y % 49 + 50))))
def get_crazy(n):
	for _ in range(n):
		print "I'm crazy!!"
		ser.write(str(unichr(14)))
		time.sleep(0.5)
		ser.write(str(unichr(0+50)))
		time.sleep(0.5)
		ser.write(str(unichr(42)))
		time.sleep(0.5)
		ser.write(str(unichr(49+50)))
		time.sleep(0.5)

def scan(i, n, m):
	for _ in range(i):
		ser.write(str(unichr(n)))
		time.sleep(0.8)
		ser.write(str(unichr(n+50)))
		time.sleep(0.8)
		ser.write(str(unichr(m)))
		time.sleep(0.8)
		ser.write(str(unichr(m+50)))
		time.sleep(0.8)


def watch(n):
	for aeon in range(n):
		for _ in range(50):
			ser.write(str(unichr(25)))
			time.sleep(0.02)
			ser.write(str(unichr(_+50)))
			time.sleep(0.02)
		for _ in range(50):
			ser.write(str(unichr(25)))
			time.sleep(0.02)
			ser.write(str(unichr(50 - _ + 50)))
			time.sleep(0.02)
