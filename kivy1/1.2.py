import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',font_size = 150)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':
    MyApp().run()
