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

def wake_up_time():
    '''alarm wake up time.'''
    h = 0
    m = 0
    time = input('when would you like to wake up? eg 6:45, 10:30 ')
    if len(time) == 5: # grabbing single digit hours before :
        hour = int(time[0:1])
        hour = h
        assert  int(time[0:1]) > 0, 'time < 1'
    if len(time) == 4: #grabbing double digit for minutes if hours single
        minutes = int(time[2:5])
        m = minutes
    elif len(time) == 6 : # grabbing double digit hours before :
        hour = int(time[1:3])
        h = hour
    assert int(time[0:2]) < 13, ' time < 12'
    else:
        minutes = int(time[3:6])
         m = minutes
    return '%d : %d ' %(h, m)

#def time_to_wake_up



#h = hour()
#m = minute()
time = wake_up_time()
print(time)
