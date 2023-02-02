class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def __str__(self):

        return f'''
{'_' * 50}
Country: {self.country}, 
Code: {str(self.code)}, 
Product: {str(self.product)}, 
Cost: {str(self.cost)}, 
Quantity: {str(self.quantity)}
{'_' * 50}'''

    def __repr__(self):
        return "%s,%s,%s,%s,%s" % (self.country,self.code,self.product,self.cost,self.quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_product(self):
        return self.product
    
    def get_code(self):
        return self.code