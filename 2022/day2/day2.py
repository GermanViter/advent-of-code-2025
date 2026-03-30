choiceValues = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

points = 0


with open("day2.txt", "r") as file:
    for line in file:
        line = line.strip().split(' ')
        elfChoice = line[0]
        playerChoice = line[1]
        print(choiceValues[playerChoice])
        points += choiceValues[playerChoice]

        rockElf = 'A'
        paperElf = 'B'
        cisorsElf = 'C'

        rockP = 'X'
        paperP = 'Y'
        cisorsP = 'Z'

        draw = ((elfChoice == rockElf) and (playerChoice == rockP) or (elfChoice == paperElf) and (playerChoice == paperP) or
                (elfChoice == cisorsElf) and (playerChoice == cisorsP))
        win = ((elfChoice == rockElf) and (playerChoice == paperP) or (elfChoice == paperElf) and (playerChoice == cisorsP) or 
               (elfChoice == cisorsElf) and (playerChoice == rockP))

        if win:
            points += 6
        elif draw:
            points += 3
print(points)
