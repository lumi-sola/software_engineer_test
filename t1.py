## Returns the part of the day based on the hour (24 hour clock).

def part_of_day(hour: int) -> str:

    if not isinstance(hour,int) or not 0 <= hour <= 23:
        raise ValueError(f"Hour must be an int in 0-23, got {hour!r}")

    if hour < 6:
        return "night"
    if hour < 12:
        return "morning"
    if hour < 18:
        return "afternoon"
    
    return "evening"


#Test Cases

print(part_of_day(1))
print(part_of_day(7))
print(part_of_day(13))
print(part_of_day(19))
print(part_of_day(25)) ## error