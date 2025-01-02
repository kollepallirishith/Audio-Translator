from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Language dictionary (language name mapped to its code)
dic = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 
    'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
    'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 
    'cebuano': 'ceb', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 
    'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 
    'french': 'fr', 'german': 'de', 'greek': 'el', 'hindi': 'hi', 'kannada': 'kn', 
    'telugu': 'te', 'tamil': 'ta'
}

def takecommand():
    """Takes audio input from the microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # listen for small periods of time
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"The User said: {query}")
            return query
        except Exception:
            return None  # In case of any recognition issue

def language_input(prompt):
    """Prompts user to input a language (source or destination)."""
    print(prompt)
    lang = input("Enter the language: ").lower()  # Taking text input from the user
    return lang

# Main Logic
# Ask the user to select source and destination languages using text input
source_lang = language_input("Enter the source language (e.g., Hindi, English):")
while not source_lang or source_lang not in dic:
    print("Source language not recognized. Try again.")
    source_lang = language_input("Enter the source language (e.g., Hindi, English):")

to_lang = language_input("Enter the language to convert to (e.g., Hindi, English):")
while not to_lang or to_lang not in dic:
    print("Destination language not recognized. Try again.")
    to_lang = language_input("Enter the language to convert to (e.g., Hindi, English):")

# Ensure valid languages were selected
source_lang_code = dic.get(source_lang)
to_lang_code = dic.get(to_lang)

# Real-time speech translation and feedback
translator = Translator()

try:
    while True:
        query = takecommand()  # Continuously listen for speech input
        if query:
            # Translate speech input
            text_to_translate = translator.translate(query, src=source_lang_code, dest=to_lang_code)
            text = text_to_translate.text
            print(f"Translated Text: {text}")

            # Text-to-Speech (immediate feedback)
            speak = gTTS(text=text, lang=to_lang_code, slow=False)
            speak.save("captured_voice.mp3")
            playsound("captured_voice.mp3")
            os.remove("captured_voice.mp3")  # Remove the audio file after playing
except KeyboardInterrupt:
    print("Translation stopped.")
