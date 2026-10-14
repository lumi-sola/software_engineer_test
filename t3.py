# Write a function called success_percentage that
# takes a list containing the success rate of each campaign and
# returns the percentage of results that are 50 or over.

def success_percentage(rates):
    if not rates:
        return 0.0
    successes = sum(1 for r in rates if r >= 50)
    return round(successes * 100 / len(rates), 2)


list_A = [42,8,23,77,27]
list_B = [74,15,19,50,33,31,47]
list_C = []

print(success_percentage(list_A)) # should return 20.0 (1 result out of 5)
print(success_percentage(list_B)) # should return 28.57 (2 results out of 7)
print(success_percentage(list_C)) # should return 0.0

#• List [42,8,23,77,13] should return 20.0 (1 result out of 5)
#• List [74,15,19,50,33,31,47] should return 28.57 (2 results out of 7)
#• Empty list should return 0.0