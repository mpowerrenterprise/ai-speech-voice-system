import os

import modules.speech_detection as SpeechDetection
from pyfirmata import Arduino

ARDUINO_PORT = os.getenv("ARDUINO_PORT", "COM4")
try:
	board = Arduino(ARDUINO_PORT)  # Change via ARDUINO_PORT env var if needed
except Exception as exc:
	raise SystemExit(f"Failed to connect to Arduino on {ARDUINO_PORT}: {exc}") from exc

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

COLOR_PINS = {
	"red": red_pin,
	"white": red_pin,
	"green": green_pin,
	"blue": blue_pin,
}


def set_all(state: int) -> None:
	red_pin.write(state)
	green_pin.write(state)
	blue_pin.write(state)


def handle_command(command: str) -> None:
	if "turn on all" in command:
		set_all(1)
		return
	if "turn off all" in command:
		set_all(0)
		return

	if "turn on" in command:
		state = 1
	elif "turn off" in command:
		state = 0
	else:
		return

	for color, pin in COLOR_PINS.items():
		if color in command:
			pin.write(state)
			return

try:
	while True:
		text = SpeechDetection.speech_to_text()

		print(text)

		if not text:
			continue

		command = text.strip().lower()
		handle_command(command)
finally:
	board.exit()
