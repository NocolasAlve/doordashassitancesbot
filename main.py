from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Dashboard(BoxLayout):
    def init(self, **kwargs):
        super().init(orientation="vertical", **kwargs)

        self.orders = []

        self.title = Label(text="📊 DoorDash Assistance Bot", font_size=22)
        self.add_widget(self.title)

        self.payout = TextInput(hint_text="Payout ($)", multiline=False)
        self.distance = TextInput(hint_text="Distance", multiline=False)
        self.time = TextInput(hint_text="Time (min)", multiline=False)

        self.add_widget(self.payout)
        self.add_widget(self.distance)
        self.add_widget(self.time)

        btn1 = Button(text="Add Order")
        btn1.bind(on_press=self.add_order)
        self.add_widget(btn1)

        btn2 = Button(text="Show Dashboard")
        btn2.bind(on_press=self.show)
        self.add_widget(btn2)

        self.output = Label(text="Ready...")
        self.add_widget(self.output)

    def add_order(self, instance):
        try:
            p = float(self.payout.text)
            d = float(self.distance.text)
            t = float(self.time.text)

            score = (p / max(d, 1)) * 10 - (t * 0.2)

            self.orders.append({
                "p": p, "d": d, "t": t, "s": round(score, 2)
            })

            self.output.text = "Order added ✔"

        except:
            self.output.text = "Invalid input"

    def show(self, instance):
        total = sum(o["p"] for o in self.orders)
        self.output.text = f"Total: ${total} | Orders: {len(self.orders)}"


class BotApp(App):
    def build(self):
        return Dashboard()


BotApp().run()
