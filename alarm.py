import datetime, time, webbrowser


def hour():
    '''hour - gets the hour from datetime,
      24 clock if (hour > 12) - 12 hours  =  time
      else hours = time
      return  time. '''
    hour = datetime.datetime.now().hour

    hours = hour
    time = hours
    if (hour > 12):


        time =  hours - 12
        assert hours > 12, 'get time hour subtraction needs fix'

    else:
        time = hours
        assert hours > 12, 'get time hour no sub needs fix'

    return  time

def minute():
    minute = datetime.datetime.now().minute
   #minute from datetime 0 to 60
    return minute

def wake_up_time():
    '''alarm wake up time.'''
    time = input('when would you like to wake up? eg 6:45, 10:30 ')
    if len(time) == 4: # grabbing single digit hours before :
        hour = time[0]
        print(hour)
    elif len(time) == 5: # grabbing double digit hours before :
        hour = time[0:2]











h = hour()
print(str(h))
m = minute()
wake = wake_up_time()
