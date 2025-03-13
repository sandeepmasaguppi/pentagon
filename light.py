class light:
    def __init__(self):
        self.brand="led"
        self.cost=100
        self.brightness=10
        self.color="white"
    def on(self):
        print("light is on")
    def off(self):
        
        print("light is off")
l1=light()
print(l1.color)
print(l1.brand)
print(l1.cost)
l1.on()
l1.off()
