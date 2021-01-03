from kivy.app import App
from kivy.core import text
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.floatlayout import FloatLayout  
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('guilayouts.kv')
import client
class Home(FloatLayout):
    pass



class MyApp(App):
# layout
    def build(self):
        layout = Home()

        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(font_size = 30, 
                      size_hint_y = None, 
                      height = 70) 
        
        btn1 = self.send()
        
        btnlayout = AnchorLayout(
            
            anchor_y = 'bottom',
            
        )
        typeandsend = BoxLayout(
                         orientation='horizontal',
                         spacing=2,
                         
                                 )
        
        typeandsend.add_widget(self.txt1)
        typeandsend.add_widget(btn1)
        btnlayout.add_widget(typeandsend)
        layout.add_widget(btnlayout)
        
        return layout

# button click function
    def sendbuttonClicked(self,btn):
        self.lbl1.text = self.txt1.text
        client.sendtext(self.txt1.text)
        self.txt1.text = ''
        
    def send(self ):
        btn = Button(
            text = "send",
            color = (1,1,1,1),
            size_hint_y = None, 
            height = 70,
            background_color = (0,.4,1,1),
            size_hint_x = .2
            ) 
            
           
        
        btn.bind(on_press=self.sendbuttonClicked)
        return btn
    def callback(self, event):
        print(f'Button is is being pressed')

app = MyApp()
app.run()