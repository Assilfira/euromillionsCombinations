import os, sys, time
from random import randint

# all combinations
allCombinations = dict()

def generate_key():
    while True:
        i = 1
        iStars = 1
        numbers = []
        stars = []

        # 5 numbers
        for i in range(1, 6):
            while True:
                value = randint(1, 50)
                if not value in numbers:
                    numbers.append(value)
                    break

        # 2 stars
        for iStars in range(1, 3):
            while True:
                star = randint(1, 12)
                if not star in stars:
                    stars.append(star)
                    break

        # order list
        numbers.sort()
        stars.sort()

        combination = ' '.join(str(n) for n in numbers) + ' + ' + ' '.join(str(s) for s in stars)

        # check if combination is unique
        if not combination in allCombinations:
            allCombinations[combination] = combination
            break


    return combination


while True:
    nb = input("Number of combinations to generate: ")
    try:
        number = int(nb)
        if (number < 0):
            print("Error. Must be a positive number")
            continue
        elif (number >= 116531800):
            print("Error. It is not possible to generate that number of combinations")
            continue
        break
    except:
        print("Error. Invalid input")


# generating combinations duration time
start_ms = time.time() * 1000

print("\nGenerating....\n")

# conitnue with the script and generate key
for num in range(1,(number+1)):
    print("("+str(num)+") "+generate_key())

# end of generating combinations duration time
end_ms = time.time() * 1000
interval = end_ms - start_ms

print("\n... and finished!\n")
print("Generated %d combination(s) in %d milliseconds" % (number, interval))
