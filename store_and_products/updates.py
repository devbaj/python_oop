import products
import store

joeys = store.Store("Joey's")

pizza = products.Product("pizza", 8, "junk food")
kiwi = products.Product("kiwi", .75, "fruit")
root_beer = products.Product("root beer", 2, "beverage")

joeys.add_product(pizza)
joeys.add_product(kiwi)
joeys.add_product(root_beer)

joeys.print_products()


print("Inflated:", joeys.inflation(.05).print_products())

print("Clearance", joeys.set_clearance(.075).print_products())

joeys.sell_product(pizza.id).print_products()