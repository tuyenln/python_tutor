#write mode to new file
# file = open("data.txt", "w")
with open("data.txt", "w") as file:
	file.write("XXX\n")
	file.write("ZZZ")



#write mode to new file
# file = open("data.txt", "w")
with open("data.txt", "w") as file:
	file.write("a\n")
	file.write("b\n")



#write mode to exist file
# file = open("data.txt", "a")
with open("data.txt", "a") as file:
	file.write("c\n")
	file.write("d")



with open("data.txt", "w") as file:
	data = file.read()
	print(data)
