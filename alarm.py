import datetime, time, webbrowser

def hour():
    '''hour - gets the hour from datetime,
      24 clock if (hour > 12) - 12 hours  =  time
      else hours = time
      return  time. '''
    hour = datetime.datetime.now().hour

    assert isinstance(hour, object)
    hours = hour
    if (hour > 12):

        time =  hours - 12
        assert hours > 12, 'get time hour subtraction needs fix'

    else:
        time = hours
        assert hours <= 12, 'get time hour no sub needs fix'

    return  time

def minute():
    minute = datetime.datetime.now().minute
   #minute from datetime 0 to 60
    return minute

def wake_up_time():
    '''alarm wake up time.'''
    alarm_time = input('time you want to wake up please: e.g 6:45, 10:30 ')

    return alarm_time







