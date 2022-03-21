from random import randint, uniform


class Tractor(object):
    power = 230.3
    workingVolume = 8.7
    revolutions = 3300
    hydraulicSystem = 4
    tireSize = 24.9
    turningRadius = 8.5
    clearance = 570
    weight = 5757.2
    fuelTankCapacity = 320
    size = 50


n = randint(1, 10)
array = []
for i in range(n):
    tractor = Tractor()
    array.append(tractor)

for i in array:
    i.power = randint(200, 300)
    i.workingVolume = uniform(5, 10)
    i.revolutions = randint(3000, 3500)
    i.hydraulicSystem = randint(2, 6)
    i.tireSize = uniform(20, 30)
    i.turningRadius = uniform(5, 10)
    i.clearance = randint(500, 600)
    i.weight = randint(5000, 6000)
    i.fuelTankCapacity = randint(300, 400)
    i.size = randint(10, 100)

for i in array:
    print(
        f"{i.size}, {i.tireSize}, {i.power}, {i.weight}, {i.turningRadius}, {i.hydraulicSystem}, {i.clearance}, {i.fuelTankCapacity}, {i.revolutions}, {i.workingVolume}"
    )

s1, s2, s3, s4, s5, s6, s7, s8, s9, s10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
length = len(array)
for i in array:
    s1 += i.size
    s2 += i.weight
    s3 += i.power
    s4 += i.revolutions
    s5 += i.workingVolume
    s6 += i.fuelTankCapacity
    s7 += i.clearance
    s8 += i.hydraulicSystem
    s9 += i.turningRadius
    s10 += i.tireSize

print(
    f"{s1 / length}, {s2 / length}, {s3 / length}, {s4 / length}, {s5 / length}, {s6 / length}, {s7 / length}, {s8 / length}, {s9 / length}, {s10 / length}"
)

