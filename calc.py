# from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
# from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Config.set('kivy', 'kveboard_mode', 'systemanddock')

Window.size = (360, 640)

class Container(GridLayout):
    formula = '0'
    label_text = ObjectProperty()
    k_1 = ObjectProperty()
    k_2 = ObjectProperty()
    k_3 = ObjectProperty()
    k_4 = ObjectProperty()
    k_5 = ObjectProperty()
    k_6 = ObjectProperty()
    k_7 = ObjectProperty()
    k_8 = ObjectProperty()
    k_9 = ObjectProperty()
    k_t = ObjectProperty()
    k_ac = ObjectProperty()
    k_y = ObjectProperty()
    k_d = ObjectProperty()
    k_m = ObjectProperty()
    k_p = ObjectProperty()

    def update_label(self):
        self.label_text.text = self.formula

    def add_number(self, instance):
        self.formula += str(instance.text)
        print(self.formula)

    def add_operation(self, instance):
        pass
        # self.formula += str(instance.text)
        # self.update_label()


class DuckyApp(MDApp):
    def build(self):
        self.formula = '0'
        self.theme_cls.theme_style = "Dark"
        return Container()


if __name__ == "__main__":
    DuckyApp().run()
