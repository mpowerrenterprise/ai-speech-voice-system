import modules.speech_detection as SpeechDetection
from pyfirmata import Arduino, util

board = Arduino('COM4') # Change 'COM4' to your Arduino's serial port

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

while True:
	text = SpeechDetection.speech_to_text()

	print(text)

	if text is not None:
		if "turn on" in text and ("red" in text or "white" in text):
			red_pin.write(1)

		elif "turn off" in text and ("red" in text or "white" in text):
			red_pin.write(0)

		elif "turn on" in text and "green" in text:
			green_pin.write(1)

		elif "turn off" in text and "green" in text:
			green_pin.write(0)

		elif "turn on" in text and "blue" in text:
			blue_pin.write(1)

		elif "turn off" in text and "blue" in text:
			blue_pin.write(0)

		elif "turn on all" in text:
			red_pin.write(1)
			green_pin.write(1)
			blue_pin.write(1)

		elif "turn off all" in text:
			red_pin.write(0)
			green_pin.write(0)
			blue_pin.write(0)