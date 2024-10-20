from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.text = ("sits left" + str(self.total))
        super().__init__(text = self.text , **kwargs)


        

    def next(self,*kwargs):
        self.current += 1 
        rest = self.total - self.current
        self.text = ("sits left" + str(rest))

