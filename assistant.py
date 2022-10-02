import sys
from voice import *
import actions
import os
import dateTime


class Bella:
    def __init__(self, ):
        self.vg = VoiceGtts()
        self.speech = ""

    def wishme(self):
        hour = int(dateTime.getDateTime()[0:2])
        print(type(hour))
        # print('yes')
        if 0 <= hour < 12:
            self.speech = "Good Morning Sir !"

        elif 12 <= hour < 18:
            self.speech = "Good Afternoon Sir !"
        else:
            self.speech = "Good Evening Sir !"
        self.speech += " how may i help you!"
        self.vg.text_to_speech(self.speech)
        self.takecommand()

    def takecommand(self, takecmd=True):
        cmd = self.vg.takecommand()
        if takecmd:
            self.handle_cmd(cmd)
        else:
            return cmd

    def handle_cmd(self, cmd):
        self.speech = cmd
        if 'change' in self.speech and 'name' in self.speech:
            self.chngusrname()
        elif 'ok bye' in self.speech:
            self.vg.speechs('end')

        else:
            obj = actions.Action()
            error = obj.handler_action(self.speech)
            if error == 'Ambiguous':
                self.vg.text_to_speech(
                    "Please specify clearly. This is ambiguous")

    def chngusrname(self):
        self.vg.text_to_speech("What should i call: ")
        temp = self.takecommand(takecmd=False)
        # while True:
        global username
        username = temp

    def next(self):
        while True:
            self.speech = self.vg.takecommand()
            if 'exit' in self.speech or 'bye' in self.speech:
                self.vg.text_to_speech('see yaa')
                sys.exit(0)
            elif 'hey assistant' in self.speech:
                cmd = self.vg.takecommand(True)
                self.handle_cmd(cmd)
            else:
                continue


if __name__ == '__main__':
    bella = Bella()
    bella.wishme()
    bella.next()
    # bella.handle_cmd()

'''

notes

'''
