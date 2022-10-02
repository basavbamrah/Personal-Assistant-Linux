import os
from gtts import gTTS
from pydub import AudioSegment, playback
import speech_recognition as sr


class VoiceGtts:
    def __init__(self):
        self.tts = None
        self.speech = ""

    def text_to_speech(self, speech):

        self.tts = gTTS(speech, lang='en', tld='co.in', slow=False)
        self.tts.save("voice.mp3")
        audio = AudioSegment.from_mp3('voice.mp3')
        playback.play(audio)

        try:
            os.remove("voice.mp3")
            return
        except:
            pass

    def takecommand(self, spk=False):

        r = sr.Recognizer()
        if spk:
            self.text_to_speech('How may i help you')
        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            # print("Unable to Recognize your voice.")
            return "None"
        # print(query)
        # # if takecmd:
        # self.speech = "u said " + query
        # self.speech = self.speech.lower()
        # self.text_to_speech(self.speech)
        # # self.vg.text_to_speech(self.speech)
        return query.lower()

