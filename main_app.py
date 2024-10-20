from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits  
from ruffier import test                                                             
from seconds import TimerWidget
from sits import Sits
from runner import Runner



name = ""
age = 7
p1 = 0
p2 = 0
p3 = 0

def check_int(number):
    try:
        return int(number)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ins = Label(text = txt_instruction)
        ageL = Label(text = "enter your age")
        nameL = Label(text = "enter your name")
        self.ageblock = TextInput(text = "7" , multiline = False)
        self.nameblock = TextInput(text = "name" , multiline = False)
        btn1 = Button(text = "Start" , size_hint = (0.3,0.2) , pos_hint = {"center_x":0.5})

        line1 = BoxLayout(size_hint = (0.8 , 0.15))
        line1.add_widget(ageL)
        line1.add_widget(self.ageblock)
        line2 = BoxLayout(size_hint = ( 0.8 , 0.15))
        line2.add_widget(nameL)
        line2.add_widget(self.nameblock)
        line3 = BoxLayout(orientation = "vertical" , spacing = 8)
        btn1.on_press = self.next
        line3.add_widget(ins)
        line3.add_widget(line1)
        line3.add_widget(line2)
        line3.add_widget(btn1)
        self.add_widget(line3)



    def next(self):
        global name , age
        age = check_int(self.ageblock.text)

        name = self.nameblock.text

        if age == False or age < 7 or age > 102 :
            self.ageblock.text = '7'
        else:
            self.manager.current = "pulse1"

        
        

        
          
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nextscreen = False
        self.widgettimer = TimerWidget(15)
        self.widgettimer.bind(finish = self.stopper)
        


        ins = Label(text = txt_test1)
        resultL = Label(text = "enter result")
        self.resultblock = TextInput(text = "0", multiline = False)
        self.resultblock.set_disabled(True)
        self.btn1 = Button(text = "next" , size_hint = (0.3,0.2) , pos_hint = {"center_x":0.5})
        line1 = BoxLayout(size_hint = (0.8 , 0.15))
        line1.add_widget(resultL)
        line1.add_widget(self.resultblock)
        line2 = BoxLayout(orientation = "vertical",spacing = 8)
        line2.add_widget(ins)
        line2.add_widget(self.widgettimer)
        line2.add_widget(line1)
        line2.add_widget(self.btn1)
        self.add_widget(line2)
        self.btn1.on_press = self.next
    def stopper(self,*kwarg):
        self.nextscreen = True
        self.resultblock.set_disabled(False) 
        self.btn1.set_disabled(False)
    def next(self):
        if self.nextscreen != True:
            self.widgettimer.start()
            self.btn1.set_disabled(True)
        else:
    
            global p1

            p1 = check_int(self.resultblock.text)

            if p1 == False or p1 <= 0 or p1 >= 120 :
                self.resultblock.text = '0'
            else :
                self.manager.current = "sits"

        
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ins = Label(text = txt_sits)
        self.btn1 = Button(text = "next" , size_hint = (0.3,0.2) , pos_hint = {"center_x":0.5})
        
        self.btn1.on_press = self.next
        self.nextscreen = False
        self.sitscounter = Sits(30)
        self.ram = Runner(total = 30 , steptime = 1.5 , size_hint = (0.4 , 1))
        self.ram.bind(finish = self.ramfin )
        self.line1 = BoxLayout(orientation = "vertical" , size_hint = (0.3 , 1))
        self.line1.add_widget(self.sitscounter)
        line2 = BoxLayout()
        line2.add_widget(ins)
        line2.add_widget(self.line1)
        line2.add_widget(self.ram)
        line3 = BoxLayout(orientation = "vertical")
        line3.add_widget(line2)
        line3.add_widget(self.btn1)
        self.add_widget(line3)
    def ramfin(self,a,b):
        self.btn1.set_disabled(False)
        self.nextscreen = True




    def next(self):
        if self.nextscreen != True:
            self.btn1.set_disabled(True)
            self.ram.start()
            self.ram.bind(value = self.sitscounter.next)
        else:
            self.manager.current = 'pulse2'
  

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widgettimer = TimerWidget(15)
        self.widgettimer.bind(finish = self.stopper)
        self.stage1 = 1
        ins = Label(text = txt_test3)
        result01 = Label(text = "result : ")
        result02 = Label(text =' result after breack :')
        self.result2box = TextInput(text = "0" , multiline = False)
        self.result1box = TextInput(text = "0" , multiline = False)
        self.result1box.set_disabled(True)
        self.result2box.set_disabled(True)

        self.btn1 = Button(text = "Finish" , size_hint = (0.3,0.2) , pos_hint = {"center_x":0.5})
        self.btn1.on_press = self.next
        line1 = BoxLayout(size_hint = (0.8,0.15))
        line1.add_widget(result01)
        line1.add_widget(self.result1box)

        line2 = BoxLayout(size_hint = (0.8,0.15))
        line2.add_widget(result02)
        line2.add_widget(self.result2box)
        line3 = BoxLayout(orientation = 'vertical',spacing = 8)
        line3.add_widget(ins)
        line3.add_widget(self.widgettimer)
        line3.add_widget(line1)
        line3.add_widget(line2)
        line3.add_widget(self.btn1)
        self.add_widget(line3)
        self.nextscreen = False
        

    def stopper(self,*kwarg):
        if self.stage1 == 1:
            self.result1box.set_disabled(False)
            self.widgettimer.restart(30)
            self.stage1 = 2
        elif self.stage1 == 2 :
            self.widgettimer.restart(15)
            self.stage1 = 3
        elif self.stage1 == 3:
            self.result2box.set_disabled(False)
            self.btn1.set_disabled(False)
            self.nextscreen = True
        

    def next(self):
        if self.nextscreen != True:
            self.widgettimer.start()
            self.btn1.set_disabled(True)
        else:
            global p2,p3

            p2 = check_int(self.result1box.text)
            p3 = check_int(self.result2box.text)
            
            if p2 == False or p3 == False or p2 <= 0 or p3 <= 0:
                self.result1box.text = '0'
                self.result2box.text = '0'

            else:
                self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.instructions = Label(text = '')

        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.main_line.add_widget(self.instructions)

        self.add_widget(self.main_line)
        
        self.on_enter = self.before

    def before(self):
        global name
        self.instructions.text = name + '\n' + test(p1,p2,p3,age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm
    
app = HeartCheck()
app.run()





