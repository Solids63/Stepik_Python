cities = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
s = cities.split()

new = list(map(lambda x: x if len(x) >= 5 else '-', s))

print(*new)
