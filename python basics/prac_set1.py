'''#  3 .  area of triangle
measure_unit = input('measured in : ')
base = float(input('base : '))
height = float(input('height : '))
area_of_triangle = .5*base*height
print(f'the area of triangle is {area_of_triangle} {measure_unit}square')

#  4 .  swap two variables
a = int(input('a : '))
b = int(input('b : '))
print(f'a : {a},b : {b} = BEFORE SWAP')
#a,b = b,a
a = a+b
b = a-b
a = a-b
print(f'a : {a},b : {b} = AFTER SWAP')

#  5 .  genarating random number
import random
print(f'random number is : {random.randint(1,100)}')

#  6 .  converting kms to miles
kms = float(input('kms : '))
#conversion factor is 1 km = 0.621371 miles
miles = kms*0.621371
print(f'the {kms} kms has {miles} miles')'''

#  7 .  celcious to fahrenheit -fahrenheit= (celcious * 9/5) + 32
celsious = float(input('celcious : '))
fahrenheit = (celsious * 9/5) + 32
print(f'{celsious} degrees celcious has {fahrenheit} degrees fahrenheit')



