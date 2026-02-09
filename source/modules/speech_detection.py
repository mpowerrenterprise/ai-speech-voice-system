import speech_recognition as sr

_RECOGNIZER = sr.Recognizer()
_RECOGNIZER.pause_threshold = 1


def speech_to_text():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            _RECOGNIZER.adjust_for_ambient_noise(source, duration=0.5)
            audio = _RECOGNIZER.listen(source, phrase_time_limit=5)  # Listen to the microphone for 5 seconds

        print("Recognizing...")
        text = _RECOGNIZER.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Error connecting to Google Web Speech API: {e}")
        return None

    except OSError as e:
        print(f"Microphone error: {e}")
        return None
