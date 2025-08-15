motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

#############

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)

##############

motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

###############

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

###############

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

del motocycles[0]
print(motocycles)

###############

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

pop_motorcycle = motocycles.pop()
print(motocycles)
print(pop_motorcycle)

################

motocycles = ['honda', 'yamaha', 'suzuki']
frist_motorcycle = motocycles.pop(1)

print(motocycles)
print(f"The first motorcycle I owned was a {frist_motorcycle.title()}.")
print(motocycles)

##################

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)

motocycles.remove('ducati')
print(motocycles)

###############

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")