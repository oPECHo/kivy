from kivy.app import App
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(text='Hello',
                      font_size=150,
                      size_hint_y=None,
                      height=200)
        l = Label(font_size=150,
                  text='Hello')
        f = FloatLayout()
        size = Window.size
        s = Scatter(pos=(90, size[1]/2 - 200))
        f.add_widget(s)
        s.add_widget(l)
        b.add_widget(t)
        b.add_widget(f)
        t.bind(text=l.setter('text'))
        return b


if __name__ == "__main__":
    TutorialApp().run()
