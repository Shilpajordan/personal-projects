from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime


class AgeCalculator(App):
    def build(self):
        '''Adding the app icon'''
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="71oA52fzYbL.png"))
        '''The user input guide text'''
        self.ageRequest = Label(
            text="Enter your date of birth (YYYY-MM-DD)",
            font_size=30,
            color="#ffffff",
            bold=True
        )
        self.window.add_widget(self.ageRequest)

        self.date = TextInput(
            multiline=False,
            padding_y=(30, 30),
            size_hint=(1, 0.7),
            font_size=30
        )
        self.window.add_widget(self.date)

        self.button = Button(
            text="Calculate Age",
            size_hint=(0.5, 0.5),
            bold=True,
            font_size=30,
            background_color=(0, 0.5, 0.5, 1)
        )
        self.button.bind(on_press=self.getAge)
        self.window.add_widget(self.button)

        return self.window

    def getAge(self, event):
        dob = self.date.text
        if dob:
            dob_date = datetime.strptime(dob, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            self.ageRequest.text = f"You are {age} years old"
        else:
            self.ageRequest.text = "Please enter a valid date of birth."


if __name__ == "__main__":
    AgeCalculator().run()



