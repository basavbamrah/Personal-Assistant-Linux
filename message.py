import pywhatkit


class SendMessage:
    def send_msg_to_one(self, text, number):
        try:
            pywhatkit.sendwhatmsg_instantly(
                number, text, wait_time=8, tab_close=True)
            return 'OK'
        except:
            return 'Error'

    def send_msg_at(self, text, number, hours, min):
        pass

    def send_msg_to_group(self, text, name):
        try:
            pywhatkit.sendwhatmsg_to_group_instantly(
                group_id=name, message=text,  tab_close=True)
        except Exception as e:

            print(e)

    def send_msg_to_grp_at(self, text, name, hour, min):
        try:
            pywhatkit.sendwhatmsg_to_group(
                group_id=name, message=text, time_hour=hour, time_min=min, tab_close=True)
        except:
            pass

    def open():
        pywhatkit.open_web()


# SendMessage().send_msg_to_group('hlo', 'Ern4NklY7d46qy1nar6emL')
