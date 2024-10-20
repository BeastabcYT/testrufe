from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation


from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    
    value = NumericProperty(0)
    finish = BooleanProperty(False)

    def __init__(self, total, steptime, auterepeat=True, bcolor=(0.73, 0.15, 0.96, 1), btext_inprogress="Присідання", **kwargs): 
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat = auterepeat
        self.text = btext_inprogress
        self.ani = Animation(pos_hint = {"top" : 1 }, duration = steptime / 2 )+ Animation(pos_hint = {"top" : 0.1 }, duration = steptime / 2 ) 
        self.btnq = Button(size_hint = (1 , 0.1) ,pos_hint = {"top" : 1})
        self.add_widget(self.btnq)
        self.ani.on_progress = self.next

    def start(self):
        self.value = 0
        self.finish = False
        self.btnq.text = self.text
        if self.autorepeat :
            self.ani.repeat = True
        self.ani.start(self.btnq)


    def next(self, widget, step):

        if step == 1:

            self.value += 1
            if self.value >= self.total:
                self.ani.repeat = False
                self.finish = True






