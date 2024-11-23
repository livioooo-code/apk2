from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def czy_oplacalne(cena_kursu, czas_dojazdu, czas_przejazdu, koszt_minuty=1, minimalny_zysk=5):
    calkowity_czas = czas_dojazdu + czas_przejazdu
    koszt_czasu = calkowity_czas * koszt_minuty
    zysk = cena_kursu - koszt_czasu
    return zysk >= minimalny_zysk


class KursApp(GridLayout):
    def __init__(self, **kwargs):
        super(KursApp, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Cena kursu (zł):"))
        self.cena_input = TextInput()
        self.add_widget(self.cena_input)

        self.add_widget(Label(text="Czas dojazdu (minuty):"))
        self.dojazd_input = TextInput()
        self.add_widget(self.dojazd_input)

        self.add_widget(Label(text="Czas przejazdu (minuty):"))
        self.przejazd_input = TextInput()
        self.add_widget(self.przejazd_input)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

        self.calculate_button = Button(text="Sprawdź opłacalność")
        self.calculate_button.bind(on_press=self.sprawdz_oplacalnosc)
        self.add_widget(self.calculate_button)

    def sprawdz_oplacalnosc(self, instance):
        try:
            cena_kursu = float(self.cena_input.text)
            czas_dojazdu = float(self.dojazd_input.text)
            czas_przejazdu = float(self.przejazd_input.text)

            if czy_oplacalne(cena_kursu, czas_dojazdu, czas_przejazdu):
                self.result_label.text = "Kurs jest opłacalny."
            else:
                self.result_label.text = "Kurs jest nieopłacalny."
        except ValueError:
            self.result_label.text = "Wprowadź poprawne dane."


class MainApp(App):
    def build(self):
        return KursApp()


if __name__ == "__main__":
    MainApp().run()
