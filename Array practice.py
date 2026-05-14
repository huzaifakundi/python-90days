car = {
    "car 1": {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    "car 2": {
        "brand": "BMW",
        "model": "X5",
        "year": 2020
    }
}

x = car.keys()
y=car.values()

print (y)
print(x) #before the change

car["color"] = "white"

print(x) #after the change
print (y)