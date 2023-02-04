from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical') #เพิ่ม code ในส้วนของ boxLayout โดยเพิ่มกำหนดการวางแนวเข้าไป
        t = TextInput(text='Hello',font_size=150)
        l = Label(font_size=150)
        b.add_widget(t) #สลับ code บรรทัดที่ 12,13 เพื่อให้ได้ผลลัพธ์ตามที่ต้องการ
        b.add_widget(l)
        t.bind(text=l.setter('text'))
        return b
if __name__ == "__main__":
 TutorialApp().run() 


 #ข้อความที่พิมพ์ใน TextInput widget ปรากฏใน Label widget เพราะการใช้ bind() method ซึ่งเชื่อมต่อคุณสมบัติ "text" ของ TextInput widget ให้กับ "text" ของ Label widget การใช้ bind() method อัพเดทคุณสมบัติ "text" ของ Label widget เมื่อคุณสมบัติ "text" ของ TextInput widget เปลี่ยนแปลง ด้วยวิธีนี้ การเปลี่ยนแปลงที่ทำกับข้อความใน TextInput widget จะปรากฏในข้อความที่แสดงใน Label widget