class product:
    
    def __init__(self,product_id, product_name, price):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        
    def applydiscount(self ):
        dis=20
        updatevalue=self.price
        updatevalue=updatevalue*(dis/100)
        print(updatevalue)
        print(self.price)
        
    def display(self):
        
        


p1.applydiscount()
        