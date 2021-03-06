dict1 = {"name": "max", "age": 14, "city": "chittagong"}
print(dict1)

dict2 = dict(name="Auvee", age=21, city="chittagong")

dict1.update(dict2)
print(dict1)

dict2 = dict1
print(dict2)

dict2["email"] = "xyz@gmail.com"
print(dict2)
print(dict1)
dict1.popitem()

print(dict1)

dict2 = dict1.copy()
print(dict2)


dict2["email"] = "xyz@gmail.com"
print(dict2)
print(dict1)

print(dict1)

dict2 = dict(dict1)
print(dict2)


dict2["email"] = "xyz@gmail.com"
print(dict2)
print(dict1)
if "name" in dict1:
    print(dict1["age"])

try:
    print(dict1["name"])
except:
    print("Error")

for key, value in dict1.items():
    print(key, value)

dict2 = dict(name="Auvee", age=21, city="chittagong")
print(dict2)

value = dict1["age"]
print(value)

dict1["email"] = "rafath.auvee@gmail.com"
print(dict1)

dict1["email"] = "rbza98@gmail.com"
print(dict1)

del dict1["name"]
print(dict1)

dict1.pop("name")
print(dict1)


value = dict1["age2"]
print(value)
