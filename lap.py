class lap():
    def __init__(self ,brand ,cost ,colour):
        self.brand=brand
        self.cost=cost
        self.colour=colour
    def on(self):
        print("lap is on")
    def off(self):
        print("lap is off")
l1=lap("asus",90,"blue")
l2=lap("mis",22,"black")
print(l1.brand)