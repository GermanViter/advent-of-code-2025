sums = []

with open("day1.txt", "r") as file:

    currentSum = 0
    for line in file:
        line = line.strip()
        if line != "":
            currentSum += int(line)
        else:
            sums.append(currentSum)
            currentSum = 0

max1 = sums.pop(sums.index(max(sums)))
max2 = sums.pop(sums.index(max(sums)))
max3 = sums.pop(sums.index(max(sums)))

print(sum([max1, max2, max3]))
