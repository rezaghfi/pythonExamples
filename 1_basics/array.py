cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
cars[0] = "Toyota"
x = len(cars)
#looping array elements
for x in cars:
  print(x)
cars.append("Porche")
cars.append("Tesla")
cars.append("Kia")
cars.append("Peugeot")
cars.append("Honda")
cars.append("Jaguar")

cars.pop(1) # delete second element of the cars array
cars.remove("BMW")
# array methods: append clear copy count extencs index insert pop remove reverse sort
cars.sort()
print(cars)