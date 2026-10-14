# Write a function called number_of_customers_in_region
# that returns a count showing how many strings
# beginning with a specific letter exist in a list of strings.

def number_of_customers_in_region(customers, letter):
    if not isinstance(letter,str) or len(letter) != 1 or not (letter.isascii() and letter.isalpha()):
        raise ValueError(f"Letter nust be a single alphabetic character (A-Z), got {letter!r} instead")

    target = letter.lower()
    return sum(1 for c in customers if c and c[0].lower() == target)


list_a = ["A_4562525", "A_8725252", "G_7252524", "C_2927359", "A_4263993"] #letter A
list_b = ["C_67673535", "B_63535425", "L_35282421", "M_6242422"] #letter Z
list_c = ["N_52662525", "H_9765522", "W_7524422", "H1334252", "I_375522"] # letter H
list_d = [] # any letter
list_e = ['', "", '', "", 'A_6565524'] # letter G

##Test Cases
print(number_of_customers_in_region(list_a, "A"))
print(number_of_customers_in_region(list_b, "Z"))
print(number_of_customers_in_region(list_c, "H"))
print(number_of_customers_in_region(list_d, "N"))
print(number_of_customers_in_region(list_e, "G"))