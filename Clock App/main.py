from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivy.clock import Clock
import datetime

from kivy.core.text import LabelBase

LabelBase.register(name="Roboto",fn_regular="Roboto/Roboto-ThinItalic.ttf",fn_bold="Roboto/Roboto-MediumItalic.ttf")


Builder.load_file("clock.kv")

class MyClock(BoxLayout):
    pass



class MyClockApp(App):
    sw_started = False
    sw_seconds = 0
    def build(self):

       self.title="Clock App"


       from kivy.core.window import Window
       Window.clearcolor=get_color_from_hex("#3E0057")
       return MyClock()

    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds+=nap

        self.root.ids.time.text=datetime.datetime.now().strftime("[b]%H[/b]:%M:%S")

        m, s = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d:[size=40]%02d[/size]'%(int(m), int(s),int(s*100%100)))

    def on_start(self):
        Clock.schedule_once(self.update_time,-1)
        Clock.schedule_interval(self.update_time,1/10)
    def start_stop_sw(self):
        self.sw_started=not self.sw_started
        if self.sw_started:
            self.root.ids.start_stop_button.text="Stop"
        else:
            self.root.ids.start_stop_button.text="Start"
    def reset_sw(self):
        self.sw_started=False
        self.sw_seconds=0
        self.root.ids.stopwatch.text = "00:00"
if __name__=="__main__":
    MyClockApp().run()
