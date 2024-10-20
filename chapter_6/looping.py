user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user.items():
    print(f"Key: {key}\nValue: {value}\n")

# loop through keys
fave_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust'
}

for name in fave_languages.keys():
    print(name.title())

#  loop through values
for language in fave_languages.values():
    print(language.upper())