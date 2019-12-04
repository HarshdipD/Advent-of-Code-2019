import math

def fuel(mass):
  mass = math.floor(mass/3)-2
  return mass

sum = 0
list_of_masses = []

with open('input.txt') as f:
    for line in f:
        list_of_masses.append(int(line))
    
for a in list_of_masses:
  sum += fuel(a)

# the anyswer
print(sum)
