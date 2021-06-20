CURRENT_YEAR = 2021
METER_TO_FEET = 3.281

firstname = input("Your first name:")
lastname = input("Your last name:")
year_born = input("Where you were born:")
height_meter = input("Your height (meter):")

year_born = int(year_born)
age = CURRENT_YEAR - year_born


# print("You are: " + str(age) + " years old in " + str(CURRENT_YEAR))

height_meter = float(height_meter)
height_meter = height_meter * METER_TO_FEET
height_meter = round(height_meter, 1)

print("\n---")
print("Your name is " + firstname + " " + lastname)
print("{2} is {0} years old in {1}".format(age, CURRENT_YEAR, firstname))
print("You are " + str(height_meter) + " feet tall")