class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        for i in range(len(self.products)):
            if id == self.products[i].id:
                print(self.products.pop(i))
                return self
    def inflation(self, percent_increase):
        for i in range (len(self.products)):
            self.products[i].update_price(percent_increase, True)
        return self
    def set_clearance(self, percent_discount):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_discount, False)
        return self
    def print_products(self):
        for i in range(len(self.products)):
            self.products[i].print_info()
        return self