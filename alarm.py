import datetime, time, webbrowser


def hour():
    hour = datetime.datetime.now().hour

    hours = hour
    time = hours
    if (hour > 12):
        time =  hours - 12
    else:
        time = hours

    return  time

def minute():
    minute = datetime.datetime.now().minute

    minutes = minute

    return minutes



def alarm(h,m):
    hour = datetime.datetime.now().hour

    hours = hour
    time = hours
    if (hour > 12):
        h = hours - 12
    else:
        h = hours

    minute = datetime.datetime.now().minute

    m = minute

    return  h +  m



h = hour()
m = minute()
wake = alarm(h,m)

def clock(h,m):
    if wake  ==  h + m :
        print('wake up')
    else:
        print('sleep')

clock(h,m)
#print(str(h) +':' + str(m))
