from kivy.lang.builder import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBoxLayout:
        orientation:'vertical'
            
        ScrollView:
            md_bg_color: app.theme_cls.primary_color
            
        MDFillRoundFlatIconButton:
            text: "GERAR"
            icon: "clover"
            line_color: (0, 0, 0, 0)
            on_press: app.press()
            
        MDBoxLayout:
            orientation:'vertical'
            
            OneLineListItem:
                id: lista
                text: "Single-line item"

'''


class MyApp(MDApp):
    def press(self):
        print("Pressed")


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


MyApp().run()
