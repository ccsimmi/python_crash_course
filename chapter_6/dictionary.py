alien = {
    'color': 'green',
    'points': 5
}

color = alien['color']
alien['name'] = 'Francis'

# dictionaries retain the order they are defined in

alien['color'] = 'yellow'

del alien['points']

#  If points exist, return else return second argument
point_value = alien.get('points', 'No point value defined')

