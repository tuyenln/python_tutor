file = open("data.txt", "w")

file.write("a\n")

file = open("data.txt", "r")

data = file.read()


print(data)