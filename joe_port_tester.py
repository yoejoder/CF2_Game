import serial

arduino = serial.Serial()

arduino.baudrate = 9600
arduino.port = '/dev/cu.usbserial-110' #change to port, find with arduino
arduino.open()


while True:
	if arduino.in_waiting:
		packet = arduino.readline()
		print(packet.decode('utf').rstrip('\n'))