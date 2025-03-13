class bottle:
    def __init__(self):
        self.name="maazza"
        self.quantity=1
        self.shape="round"
        self.price=80
    def open(self):
        print("open the cap")
    def close(self):
        print("close the bottle")

b1=bottle()
print(b1.name)
print(b1.price)
print(b1.quantity)

b1.open()
        