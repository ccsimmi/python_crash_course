# magicians = ['alice', 'david', 'carolina']
# for mage in magicians:
#     print(mage)

# for value in range(1, 5):
#     print(value)

numbers = list(range(1, 6))

evenNumbers = list(range(0, 11, 2))
# print(evenNumbers)

squares = []
for v in range(1, 11):
        square = v **2
        squares.append(square)

# print(squares)

# List comprehensions generate the above list in one line of code
squared = [value**2 for value in range(1, 11)]