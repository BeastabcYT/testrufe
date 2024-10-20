from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class TimerWidget(Label):
    finish = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.finish = False
        text = "time gone:" + str(self.current)
        super().__init__(text = text)



    def restart(self, total, **kwargs):
        self.finish = False
        self.total = total 
        self.current = 0
        self.text = "time gone:" + str(self.current)
        self.start()

    def start(self):
        Clock.schedule_interval(self.change,1)


    def change(self, dt):
        self.current += 1 
        self.text = "time gone :" + str(self.current)
        if self.current >= self.total:
            self.finish = True
            return False
