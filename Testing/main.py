# This is a sample Python script.
import math

#if __name__ == '__main__':

i = 0
while i < 1:
    i += 1

    if i < 8:
        print("For lite")
    else:
        print("ok")

    for a in 'Hallo':
        print('bokstav', a)

    for i in range(1, 10, 2):
        print(i)

    mix = ['apple', 'banana', 44, 2]
    for x in mix:
        print(x)

    print(len(mix)) #lengden til listen

inlist = ["hei", "hade"]
mix2 = [[2, 8], 'banana', inlist, "blueberry"]
print(mix2[2])
print(mix2[2][0])

# legger sammen to lister
b = [1, 2]
c = [3, 4]
d = b + c
print(d)
print(d[1:3])  # fra og med til

aa = (1, 2, 3)
ab = (2, 3, 4)
if aa > ab:
    print(aa)
else:
    print(ab)

car = {
    'brand': 'tesla',
    'year': 2022
}
print(car.keys())

