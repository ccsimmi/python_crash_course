cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'subaru':
        print(car.upper())
    else:
        print(car.title())

# check whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_toppings:
    print(f"we got the {requested_toppings[0]}!")

# now the reverse - not in the list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
