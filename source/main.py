import os

import modules.speech_detection as SpeechDetection
from pyfirmata import Arduino

ARDUINO_PORT = os.getenv("ARDUINO_PORT", "COM4")
board = Arduino(ARDUINO_PORT)  # Change via ARDUINO_PORT env var if needed

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

try:
	while True:
		text = SpeechDetection.speech_to_text()

		print(text)

		if text is None:
			continue

		command = text.strip().lower()
		if "turn on all" in command:
			red_pin.write(1)
			green_pin.write(1)
			blue_pin.write(1)

		elif "turn off all" in command:
			red_pin.write(0)
			green_pin.write(0)
			blue_pin.write(0)

		elif "turn on" in command and ("red" in command or "white" in command):
			red_pin.write(1)

		elif "turn off" in command and ("red" in command or "white" in command):
			red_pin.write(0)

		elif "turn on" in command and "green" in command:
			green_pin.write(1)

		elif "turn off" in command and "green" in command:
			green_pin.write(0)

		elif "turn on" in command and "blue" in command:
			blue_pin.write(1)

		elif "turn off" in command and "blue" in command:
			blue_pin.write(0)
finally:
	board.exit()
