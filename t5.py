# Given a list of n campaign priorities, e.g. [1,0,2,3]
# Return the minimum number of Energy Specialists
# needed to complete the telephone surveys

def min_energy_specialists(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    total = 1
    up = down = peak = 0

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            up += 1
            down = 0
            peak = up
            total += up + 1
        elif ratings[i] < ratings[i - 1]:
            up = 0
            down += 1
            total += down + (down > peak)
        else:
            up = down = peak = 0
            total += 1

    return total

## Test Cases

ratings1 = [1,0,2]
ratings2 = [1,2,2]

print(min_energy_specialists(ratings1))
#Output: 5

print(min_energy_specialists(ratings2))
#Output: 4