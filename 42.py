def enter_input(prompt):
	input_value = input(prompt)
	input_value = int(input_value)
	return input_value

def write_to_file(number):
	with open("data.txt", "w") as file:
		for i in range(number):
			file.write(str(number- i) + "\n")

def read_file_list():
	numbers = []
	with open("data.txt", "r") as file:
		numbers = file.read().split("\n")
		numbers.pop()
	return numbers



def main():
	number = enter_input("Enter your number: ")
	write_to_file(number)
	data = read_file_list()
	for i in range(len(data)):
		print("Line " + str(i+1) + ":" + data[i])

main()