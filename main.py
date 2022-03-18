#alarm clock OOP
from alarm_clock import Alarm_Clock

clock = Alarm_Clock("11pm", "7am")
print(clock.current_time)

clock.change_current_time()

clock.change_alarm()

clock.alarm_off()



