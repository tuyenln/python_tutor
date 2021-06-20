class Student:
	def __init__(self, name, age, math, lit):
		self.name 	= name
		self.age 	= age
		self.math 	= math
		self.lit 	= lit

	def average_score(self):
		return (self.math + self.lit) / 2;

	def print_info(self):
		ave = str(self.average_score())
		print("Student name " + self.name + " diem "+ ave)


students = []
s1 = Student("David", 21, 10, 7)
s2 = Student("jame", 23, 4, 7)
s3 = Student("Luis", 25, 10, 6)

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
	students[i].print_info()
