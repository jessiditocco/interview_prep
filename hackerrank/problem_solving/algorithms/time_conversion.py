def timeConversion(s):
    #
    time = s.split(":")
    hour = time[0]
    minutes = time[1]
    seconds = time[2][0:2]
    am_or_pm = time[2][2:]


    if am_or_pm == "AM" and hour == "12":
        print "00:{}:{}".format(minutes, seconds)

    elif am_or_pm == "AM" and 1 <= int(hour) < 11:
        print "{}:{}:{}".format(hour, minutes, seconds)

    elif am_or_pm == "PM" and hour == "12":
        print "12:{}:{}".format(minutes, seconds)

    elif am_or_pm == "PM" and 1 <= int(hour) < 12:
        hour = int(hour) + 12
        print "{}:{}:{}".format(hour, minutes, seconds)
    

if __name__ == '__main__':
    s = raw_input()

    result = timeConversion(s)