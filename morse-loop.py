import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

def morse(nilai):
	banyaksimbol = nilai.split()
	for simbol in banyaksimbol:
		if(simbol =="*"):
			titik()
		elif(simbol == "-"):
			garis()
		else:
			jeda()

def garis():
	GPIO.output(8, GPIO.HIGH)
	sleep(1.5)
	GPIO.output(8, GPIO.LOW)
	sleep(1.5)

def titik():
	GPIO.output(8, GPIO.HIGH)
	sleep(1)
	GPIO.output(8, GPIO.LOW)
	sleep(1)

def jeda():
	sleep(1.5)

# try: except namainput: "Perintah untuk interupsi dengan media input"
try:

while 1: "Perintah untuk loop"
	while 1:
		morse("* * */- - -/* * *")
except KeyboardInterrupt:
	GPIO.cleanup(8)
