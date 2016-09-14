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
        assert hours <= 12, 'get time hour no sub needs fix'

    return  time

def minute():
    minute = datetime.datetime.now().minute
   #minute from datetime 0 to 60
    return minute



def wake_up_time(h, m):
    '''alarm wake up time.'''
    time = input('when would you like to wake up? eg 6:45, 10:30 ')
    if len(time) == 4: # grabbing single digit hours before :
        hour = int(time[0])
        assert  int(time[0]) > 0, 'time < 1'
    elif len(time) == 5: # grabbing double digit hours before :
        hour = int(time[0:2])
        assert int(time[0:2]) < 13, ' time < 12'
    minutes = int(time[3:6])

    #wake_up = time.strftime('%I + : + %M', t % h, m)



h = hour()
m = minute()
wake_up_time(h,m)
