import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source, phrase_time_limit=5)  # Listen to the microphone for 5 seconds

        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Error connecting to Google Web Speech API: {e}")
        return None
