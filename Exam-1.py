chai_types = {
    "Masala": "spicy", "Malai": "sweet", "Ginger": "Zesty", "Green":"Fresh" 
}

# .get()
# .pop()
# .popitem()
# .copy()
# .items()

print(chai_types.get("Masala"))
chai_types["Green"] = "Salty"
print(chai_types)
for chai in chai_types:
    print(chai)
for key, value in chai_types.items():
    print(key, value)
for chai in chai_types:
    print(chai_types[chai])

print(len(chai_types))
chai_types["Earl Grey"] = "Citrus"
print(chai_types)
chai_types.pop("Ginger")
chai_types.popitem()
print(chai_types)
chai_types_copy = chai_types.copy()
print(chai_types_copy)

tea_shop = {
    "chai": {"Masala" : "spicy", "Ginger" : "Zesta"}, 
    "Tea": {"Green" : "Mild", "Black" : "strong"}
}

print(tea_shop)
tea_shop["chai"]

print(tea_shop["chai"]["Ginger"])

tea_shop["chai"]["Ginger"] = "Zesty"
print(tea_shop["chai"]["Ginger"])

squared_num = {x: x**2 for x in range(6)}
print(squared_num)
squared_num.clear()

squared_num
print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]
print(keys)

default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys, keys)
print(new_dict)






