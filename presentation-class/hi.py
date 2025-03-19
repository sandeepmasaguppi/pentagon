class product:
    
    def __init__(self,product_id, product_name, price):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        
    def display(self):
        print(f"product_id:{self.product_id}")
        print(f"product name:{self.product_name}")
        print(f"price: {self.price}")
        
    def applydiscount(self ):
        dis=50
        updatevalue=self.price
        updatevalue=updatevalue*(dis/100)
        print(updatevalue)
        print(self.price)
        
p=product(101,"san",4000)
p.display()
p.applydiscount()
        
        