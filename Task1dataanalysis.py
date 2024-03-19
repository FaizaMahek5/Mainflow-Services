colors = ['red', 'green', 'blue', 'yellow']
colors.append('purple')
print(colors)
colors.remove('green')
print(colors)
colors[1] = 'orange'
print(colors)

countries_capitals = {'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}
countries_capitals['Germany'] = 'Berlin'
print(countries_capitals)
del countries_capitals['UK']
print(countries_capitals)
countries_capitals['France'] = 'Marseille'
print(countries_capitals)

prime_numbers = {2, 3, 5, 7, 11}
prime_numbers.add(13)
print(prime_numbers)
prime_numbers.remove(5)
print(prime_numbers)
prime_numbers.remove(2)
prime_numbers.add(17)
print(prime_numbers)
