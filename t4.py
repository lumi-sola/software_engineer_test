# In t4 write a function called complete_tariff
# which takes 2 strings as arguments.

def complete_tariff(code, customer_type):
    n = len(customer_type)
    gap = "-" * n
    if n == 0 or code.count("-") != n or gap not in code:
        return None

    return code.replace(gap, customer_type, 1)


#Test Cases

print(complete_tariff("NEXT_2YR_FIXED_--------_V8", "BUSINESS"))
# Output: NEXT_2YR_FIXED_BUSINESS_V8

print(complete_tariff("VARIABLE_-----------_ENERGY", "RESIDENTIAL"))
# Output: VARIABLE_RESIDENTIAL_ENERGY

print(complete_tariff("TBC_1YR_FIXED_----", "OCCUPIER"))
# Output: None

print(complete_tariff("---_VARIABLE", "SME"))
# Output: SME_VARIABLE

print(complete_tariff("NEXT_1YR_FIXED_--------_V3", "SME"))
# Output: None

print(complete_tariff("A-B--", "SME"))
# Output: None   (3 dashes, but not next to each other)


#"NEXT_2YR_FIXED_--------_V8" and "BUSINESS" would return "NEXT_2YR_FIXED_BUSINESS_V8"
#"VARIABLE_-----------_ENERGY" and "RESIDENTIAL" would return "VARIABLE_RESIDENTIAL_ENERGY"
#"TBC_1YR_FIXED_----" and "OCCUPIER" would return None
#"---_VARIABLE" and "SME" would return "SME_VARIABLE
#"NEXT_1YR_FIXED_--------_V3" and "SME" would return None