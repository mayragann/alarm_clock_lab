class Alarm_Clock:
    def __init__(self, time, alarm_time):
        self.current_time= time
        self.alarm_is_on = False
        self.set_alarm_time = alarm_time

    def change_current_time(self):
        self.current_time = input("What do you want to set your new time to?: ")
        print("This is the new time:", self.current_time)
        
         
    def change_alarm(self):
        self.alarm_is_on = True
        print('Alarm is on')

    def alarm_off(self):
        self.alarm_is_on = False
        print ('Alarm is off')
        
    
    def alarm_time_change(self, alarm_time):
        self.set_alarm_time = input("What time do you want your alarm set to?")
        self.set_alarm_time = alarm_time
        if self.set_alarm_time == self.set_alarm_time:
            print("That is the current time")
        else:
            print("Time has been changed to:", self.current_time)
    