# import message
import window
import voice
import webbrowser
import wikipedia
from database import HandleDatabase as db
from urllib.request import urlopen
import apis
import os
import multiprocessing


class Action:
    def __init__(self):
        print('yes Action')
        self.speech = ""
        self.vg = voice.VoiceGtts()
        self.obj = window.Window()
        # self.msg = message.SendMessage()

    def handler_action(self, speech):
        print('yes')
        self.speech = speech

        if 'wikipedia' in self.speech:

            self.speech = self.speech.replace('wikipedia', "")
            try:
                results = wikipedia.summary(self.speech)
            except wikipedia.DisambiguationError:
                print('yes exp')
                return 'Ambiguous'
            self.obj.print_text(results)

        elif 'search' in self.speech:
            self.speech = self.speech.replace('search', "")
            webbrowser.open(self.speech)

        elif 'open youtube' in self.speech:

            self.vg.text_to_speech("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in self.speech:
            self.vg.text_to_speech("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in self.speech:
            self.vg.text_to_speech(
                "Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'todo list' in self.speech or 'to do list' in self.speech:
            multiprocessing.Process(target=self.obj.todo).start()

        # elif 'whatsapp web' in self.speech:
        #     self.msg.open()

        # elif 'send message' in self.speech:
        #     print('yes')
        #     self.vg.text_to_speech('whom do you want to send:')
        #     name = self.vg.takecommand()

        #     self.vg.text_to_speech("what fo you want to send:  ")
        #     msg = self.vg.takecommand()

        #     number = db().fetch_number(name.strip())
        #     print(number)
        #     # # print(number)
        #     for i in number:

        #         print(i)
        #         if i:
        #             try:
        #                 print(self.msg.send_msg_to_one(msg, i))
        #                 break
        #             except Exception as e:

        #                 print(e)
        elif 'shutdown' in self.speech:
            os.system('shutdown now')
        elif 'log off' in self.speech:
            os.system('gnome-session-quit')

        elif 'gesture control' in self.speech:
            # under progress
            pass
        elif 'update contact' in speech:
            db().load_vcf()
            pass
        elif 'solve math' in speech:

            pass
        elif 'news headlines' in speech:
            apis.headlines()

        elif 'news on' in speech:
            pass


Action().handler_action('news headlines')
# Action().handler_action('shutdown')
# Action().handler_action('log off')
