# Import necessary modules and types
from type import VociesType
import os

from gtts import gTTS  # Google Text-to-Speech API
import pyttsx3  # For text-to-speech conversion using pyttsx3 engine


class TextToAudio:

    def convert_text_to_audio(self, text: str, engin:str="gtts",language: str = 'en', output_file: str = 'output.wav', voice=None):
        """
        Convert text to speech using gTTS (Google Text-to-Speech) and save it as an audio file.

        Args:
            text: 
                The input text to convert to speech (str).

            language: 
                The language of the input text (str).

            output_file: 
                The path to save the output audio file (str).

            tld:
                The top-level domain (TLD) for the gTTS API (str).

        Returns:
            None
        """
        if engin=="gtts":
            self.textToAudioGtts(text, language, output_file, tld=voice if voice else "com")
        elif engin=="pyttsx3":
            self.textToAudioPyttsx3(text, language, output_file, voice)
        

    # Function to convert text to speech using gTTS (Google Text-to-Speech)
    def textToAudioGtts(text: str, language: str = 'en', output_file: str = 'output.wav', tld:str="com"):
        """
        Convert text to speech using gTTS (Google Text-to-Speech) and save it as an audio file.

        Args:
            text: 
                The input text to convert to speech (str).

            language: 
                The language of the input text (str).

            output_file: 
                The path to save the output audio file (str).

            tld:
                The top-level domain (TLD) for the gTTS API (str).

        Returns:
            None
        """
        tts = gTTS(text=text, lang=language, tld=tld)
        tts.save(output_file)
       

        

    # Function to convert text to speech using pyttsx3 engine
    def textToAudioPyttsx3(text: str, language: str = 'en', output_file: str = 'output.mp3', voice=None):
        """
        Convert text to speech using pyttsx3 and save it as an audio file.

        Args:
            text: 
                The input text to convert to speech (str).

            language: 
                The language of the input text (str).

            output_file: 
                The path to save the output audio file (str).

        Returns:
            None
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume level
        if voice:
            engine.setProperty('voice', voice)
        engine.setProperty('language', language)
        engine.save_to_file(text, output_file)
        engine.runAndWait()

    def allVoiceInGTTS():
        """
        Get all available voices in the gTTS API.

        Returns:
            List[str]: A list of available voices.
        """
        voices:VociesType = [
            {"id": "com.au", "name": "English (Australia)", "languages": "en"},
            {"id": "co.uk", "name": "English (United Kingdom)", "languages": "en"},
            {"id": "us", "name": "English (United States)", "languages": "en"},
            {"id": "ca", "name": "English (Canada)", "languages": "en"},
            {"id": "co.in", "name": "English (India)", "languages": "en"},
            {"id": "ie", "name": "English (Ireland)", "languages": "en"},
            {"id": "co.za", "name": "English (South Africa)", "languages": "en"},
            {"id": "ca", "name": "French (Canada)", "languages": "fr"},
            {"id": "fr", "name": "French (France)", "languages": "fr"},
            {"id": "com", "name": "Mandarin (China Mainland)", "languages": "zh-CN"},
            {"id": "com", "name": "Mandarin (Taiwan)", "languages": "zh-TW"},
            {"id": "com.br", "name": "Portuguese (Brazil)", "languages": "pt"},
            {"id": "pt", "name": "Portuguese (Portugal)", "languages": "pt"},
            {"id": "com.mx", "name": "Spanish (Mexico)", "languages": "es"},
            {"id": "es", "name": "Spanish (Spain)", "languages": "es"},
            {"id": "us", "name": "Spanish (United States)", "languages": "es"},
        ]
        return voices
        
    
    def allVoiceInPyttsx3():
        """
        Get all available voices in the pyttsx3 engine.

        Returns:
            List[str]: A list of available voices.
        """
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        voices:VociesType= [{"id":voice.id,"name": voice.name,"languages":voice.languages[0]} for voice in voices]

        return voices
        
    


    

