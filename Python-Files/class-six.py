# Create a list of dictionaries called products with a name and a price
products = [
    {"name": "Product 1", "price": 10.99},
    {"name": "Product 2", "price": 20.49},
    {"name": "Product 3", "price": 15.99}
]

# Delete the price of the second key item
del products[1]["price"]

# Display the updated list of products
print(products)

products[1]["color"] = "Silver"
print(products)

# Adding new items: Given a list of dictionaries representing products, write a function to add a new product to the list.

# def new_items(products):
#     new_item_key = str(input("Enter the name of the new key: "))
#     new_item_value = int(input("Enter the price of the product: "))  # You need to define the value for the new key

#     for item in products:
#         item[new_item_key] = new_item_value

#     return products

#Updating prices: Write a program that allows users to update the price of a specific product in the list of dictionaries.

# updated_products = new_items(products)
# print(updated_products)

# def update_price(price):
#     product_name = str(input("Enter the name of the product: "))
#     new_price = int(input("Enter the price of the product: "))

#     for item in products:
#         item[product_name] = new_price

#     return products

# updated_products = update_price(products)
# print(updated_products)

# def remove_product(products, product_name):
#     # Create a new list without the product to be removed
#     updated_products = [product for product in products if product['name'] != product_name]
#     return updated_products

# # Remove "Product 2" from the list of products
# updated_products = remove_product(products, "Product 2")
# print(updated_products)












