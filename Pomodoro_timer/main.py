import time 
from notifypy import Notify
from playsound import playsound

pomodori = int(input('Quanti pomodori vuoi fare? '))

t = int(input('Di quanti minuti deve essere? ')) 
t *= 60

riposo = int(input('Quanti minuti di riposo vuoi fare? '))
riposo *= 60

while pomodori:

    def countdown(t):
        while t: 
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    
        notification = Notify()
        notification.title = "POMODORO TIMER"
        notification.message = "È tempo di una pausa"
        notification.send()

    def secondo_countdown(riposo):
        while riposo:
            mins, secs = divmod(riposo, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            riposo -= 1

        notification = Notify()
        notification.title = "POMODORO TIMER"
        notification.message = "È arrivato il momento di studiare!"
        notification.send()
    
    countdown(t)
    secondo_countdown(riposo)

