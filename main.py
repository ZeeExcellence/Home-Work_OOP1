class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def rate_lecturer(self, teacher, course, grade):  # Оценка лекций от студентов
		if isinstance(teacher, Lecturer) and course in self.courses_in_progress and course in teacher.courses_attached:
			if course in teacher.grades:
				teacher.grades[course] += [grade]
			else:
				teacher.grades[course] = [grade]
		else:
			return 'Ошибка'

	def get_avg(self):
		self.numbers = []
		for key, value in self.grades.items():
			for number in value:
				self.numbers.append(number)
		res = sum(self.numbers) / len(self.numbers)
		return round(res, 2)

	def __str__(self):  # Крутая "ПАСТА"
		res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_avg()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
		return res

	def __lt__(self, other):
		if not isinstance(other, Student):
			print('Ошибка')
			return
		return self.get_avg() < other.get_avg()


class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []


class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades = {}

	def get_avg(self):
		self.numbers = []
		for key, value in self.grades.items():
			for number in value:
				self.numbers.append(number)
		res = sum(self.numbers) / len(self.numbers)
		return round(res, 2)

	def __str__(self):
		res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg()}'
		return res

	def __lt__(self, other):
		if not isinstance(other, Lecturer):
			print('Ошибка')
			return
		return self.get_avg() < other.get_avg()


class Reviewer(Mentor):
	def __str__(self):
		res = f'Имя: {self.name}\nФамилия: {self.surname}'
		return res

	def rate_hw(self, student, course, grade):  # Оценка домашки Ревьюером
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'


student_1 = Student('Эзра', 'Бриджер', 'Мужской')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['SQL']

student_2 = Student('Асока', 'Тано', 'Женский')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['С++']

student_3 = Student('Эйла', 'Секура', 'Женский')
student_3.courses_in_progress += ['Java']
student_3.finished_courses += ['Ruby']

student_4 = Student('Люк', 'Скайокер', 'Мужской')
student_4.courses_in_progress += ['Java']
student_4.finished_courses += ['CSS']

reviewer_1 = Reviewer('Северус', 'Снейп')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Минерва', 'МакГонагалл ')
reviewer_2.courses_attached += ['Java']

lecturer_1 = Lecturer('Оби-ван', 'Кеноби')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Мейс', 'Винду')
lecturer_2.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_4, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Java', 6)
reviewer_2.rate_hw(student_3, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Java', 6)
reviewer_2.rate_hw(student_4, 'Java', 10)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_3.rate_lecturer(lecturer_2, 'Java', 6)
student_4.rate_lecturer(lecturer_2, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_3.rate_lecturer(lecturer_2, 'Java', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 7)

students_list = [student_1, student_2, student_3, student_4]
lecturer_list = [lecturer_1, lecturer_2]


def get_avg(student, course):
	some_list = []
	for person in student:
		for key, value in person.grades.items():
			if key == course:
				some_list += value
	return f'Средняя оценка у студентов по предмету {course}: {round(sum(some_list) / len(some_list), 2)}'


def get_avg_lecturer(lecturer, course):
	some_list = []
	for person in lecturer:
		for key, value in person.grades.items():
			if key == course:
				some_list += value
	return f'Средняя оценка у лекторов по предмету {course}: {round(sum(some_list) / len(some_list), 2)}'


print(get_avg(students_list, 'Python'))
print(get_avg(students_list, 'Java'))
print(get_avg_lecturer(lecturer_list, 'Java'))
print(get_avg_lecturer(lecturer_list, 'Python'))
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1)
print()
print(student_2)
print()
print(student_3)
print()
print(student_4)
print()
print(lecturer_2 < lecturer_1)
print(lecturer_1 > lecturer_2)