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

gerder_input = input("Are you male (yes/no): ")

if gerder_input == "yes":
	is_male = True
elif gerder_input == "no":
	is_male = False
else:
	is_male = None


if is_male is None:
	print("Invalid Answer")
elif is_male == True:
	if height_meter > 6.5:
		print("You are very tall as a man")
	elif height_meter > 6.0:
		print("You are tall")
	else:
		print("You are short as a man")
elif is_male == False:
	if height_meter > 5.7:
		print("You are tall as a girl")
	else:
		print("You are short as a girl")
else:
	print("System error, variable 'is_male' is not correct")