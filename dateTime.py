import datetime

def getDateTime():
    hour = (datetime.datetime.now())
    # print(hour)
    current_time = hour.strftime("%H:%M")
    # print("Current Time =", current_time)
    return current_time
    #
def fun():
    pass

# getDateTime()
