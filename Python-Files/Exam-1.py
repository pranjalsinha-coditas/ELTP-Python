chai_types = {
    "Masala": "spicy", "Malai": "sweet", "Ginger": "Zesty", "Green":"Fresh" 
}

# .get()
# .pop()
# .popitem()
# .copy()
# .items()


# {'Masala': 'spicy', 'Malai': 'sweet', 'Green': 'Salty'}
# {'Masala': 'spicy', 'Malai': 'sweet', 'Green': 'Salty'}
# {'chai': {'Masala': 'spicy', 'Ginger': 'Zesta'}, 'Tea': {'Green': 'Mild', 'Black': 'strong'}}
# Zesta
# Zesty
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# {}
# {'Lemon', 'Masala', 'Ginger'}
# {'Lemon': 'Delicious', 'Masala': 'Delicious', 'Ginger': 'Delicious'}
# {'Lemon': {'Lemon', 'Masala', 'Ginger'}, 'Masala': {'Lemon', 'Masala', 'Ginger'}, 'Ginger': {'Lemon', 'Masala', 'Ginger'}}
print(chai_types.get("Masala"))
# spicy
chai_types["Green"] = "Salty"
print(chai_types)
# {'Masala': 'spicy', 'Malai': 'sweet', 'Ginger': 'Zesty', 'Green': 'Salty'}
for chai in chai_types:
    print(chai)
# Masala
# Malai
# Ginger
# Green
for key, value in chai_types.items():
    print(key, value)
# Masala spicy
# Malai sweet
# Ginger Zesty
# Green Salty
for chai in chai_types:
    print(chai_types[chai])
# spicy
# sweet
# Zesty
# Salty
print(len(chai_types))
# 4
chai_types["Earl Grey"] = "Citrus"
print(chai_types)
# {'Masala': 'spicy', 'Malai': 'sweet', 'Ginger': 'Zesty', 'Green': 'Salty', 'Earl Grey': 'Citrus'}
chai_types.pop("Ginger")
# {'Masala': 'spicy', 'Malai': 'sweet', 'Green': 'Salty'}
chai_types.popitem()
# {'Masala': 'spicy', 'Malai': 'sweet', 'Green': 'Salty'}
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
keys = {"Masala", "Ginger", "Lemon"}
print(keys)
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)








