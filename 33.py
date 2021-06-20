import datetime

def ask_yes_no(pronpt):
	while True:
		answer = input(pronpt)
		if answer == "yes":
			return True
		elif answer	== "no":
			return False
		else:
			continue

def calc_age(year_born):
	now = datetime.datetime.now()
	current_year = now.year
	return current_year - year_born

def conver_meter_to_feet(height_meter):
	METER_TO_FEET = 3.281
	height_meter = height_meter * METER_TO_FEET
	height_meter = round(height_meter, 1)
	return height_meter

def print_height_info(height_meter, is_male):
	if is_male == True:
		if height_meter > 6.5:
			print("You are very tall as a man")

		elif height_meter > 6.0:
			print("You are tall")
		else:
			print("You are short as a man")
	if is_male == False:
		if height_meter > 5.7:
			print("You are tall as a girl")
		else:
			print("You are short as a girl")

def print_persion_info(firstname, lastname, age, height_meter, is_male):
	now = datetime.datetime.now()
	current_year = now.year
	print("\n---")
	print("Your name is " + firstname + " " + lastname)
	print("{2} is {0} years old in {1}".format(age, current_year, firstname))
	print("You are " + str(height_meter) + " feet tall")

	print_height_info(height_meter, is_male)

def ask_persion_info():
	firstname = input("Your first name:")
	lastname = input("Your last name:")
	year_born = int(input("Where you were born:"))
	height_meter = float(input("Your height (meter):"))
	is_male = ask_yes_no("Are you male (yes/no): ")
	return firstname, lastname, year_born, height_meter, is_male

def main():

	firstname, lastname, year_born, height_meter, is_male = ask_persion_info()
	age = calc_age(year_born)
	height_meter =conver_meter_to_feet(height_meter)
	print_persion_info(firstname, lastname, age, height_meter, is_male)



main()
