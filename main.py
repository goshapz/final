import math


def p(x,  y, z):
    return 1/2 * (x + y + z)


def s(x, y, z):
    return math.sqrt(p(x, y, z) * (p(x, y, z)-x) * (p(x, y, z)-y) * (p(x, y, z)-z))


def trch(x, y, z):
    return bool((x + y > z) and (y + z > x) and (z + x > y))


s1 = 'Undefined'
s2 = 'Undefined'
s3 = 'Undefined'

storony = input('Enter sides splited with space: ')
sides = storony.split(' ')
for i, value in enumerate(sides):
    sides[i] = int(value)
sides.sort()
print(sides)

m = 0

for i in range(len(sides)):
    if sides[i] <= 0:
        print('index out of range!')
        exit()

for i in range(1, len(sides)-1):
    if trch(sides[i-1], sides[i], sides[i+1]) is True:
         n = s(sides[i-1], sides[i], sides[i+1])
         if n > m:
            m = n
            s1 = sides[i - 1]
            s2 = sides[i]
            s3 = sides[i + 1]

print('a =', s1, 'b =', s2, 'c =', s3)
print('A perimetr of the triangle is :', 2 * p(s1, s2, s3))
print('An area of the triangle is :', m)
