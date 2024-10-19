bicycles = ['trek', 'cannondale', 'redline', 'specialised']
# print(bicycles[0])

# get last element
# print(bicycles[-1])

message = f"My first biycle was a {bicycles[0].title()}"
# print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
del motorcycles[0]
motorcycles.insert(1, 'honda');
motorbike = motorcycles.pop(2)
motorcycles.remove('ducati')
# print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
#cars.sort(reverse=True)
#sorted(cars) // does not permanently sort
cars.reverse()
print(cars)
length = len(cars)