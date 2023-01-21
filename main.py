class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and \
                course in self.courses_in_progress and grade <= 10:
            lectur.grades += [grade]
        else:
            return print("Ошибка")

    def get_average_grade(self):
        s = 0
        count = 0
        if self.grades:
            for grades in self.grades.values():
                s += sum(grades)
                count += len(grades)
            return round(s / count, 2)
        else:
            return print('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за ДЗ: {self.get_average_grade()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
              f'Завершенные курсы: {self.finished_courses} \n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_average_grade() < other_student.get_average_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже чем {self.name} {self.surname}')
        return compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades) :.2f} \n'
        return res

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res

    def __lt__(self, lectur):
        if not isinstance(lectur, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare_lect = sum(self.grades) / len(self.grades) < sum(lectur.grades) / len(
                lectur.grades)
            if compare_lect:
                print(f'{self.name} {self.surname} хуже {lectur.name} {lectur.surname}')
            else:
                print(f'{lectur.name} {lectur.surname} хуже {self.name} {self.surname}')
        return compare_lect

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res

def _average_grade(student_list, course):
    suma = 0

    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                suma += sum(grades) / len(grades)
    return round(suma / len(student_list), 2)

def _average_grade_list(lecturer_list):
    total_sum = 0
    for lecturer in lecturer_list:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return round(total_sum / len(lecturer_list), 2)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']

bad_student = Student('Parker', 'Simpson', 'M')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.grades['Python'] = [5, 7, 9]
bad_student.grades['Git'] = [9,7]

best_reviewer = Reviewer('Jhon', 'Linden')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Git']

best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(bad_student, 'Python', 8)
best_reviewer.rate_hw(best_student, 'Git', 10)
best_reviewer.rate_hw(bad_student, 'Git', 7)

first_lecturer = Lecturer('Mary', 'Mann')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

some_lecturer = Lecturer('Tom', 'Raddl')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

best_student.rate_lectur(first_lecturer, 'Python', 10)
best_student.rate_lectur(some_lecturer, 'Git', 8)
bad_student.rate_lectur(first_lecturer, 'Python', 6)
bad_student.rate_lectur(some_lecturer, 'Git', 9)

print(best_student.grades)
print(bad_student.grades)
print(first_lecturer.grades)
print(some_lecturer.grades)
print(bad_student < best_student)
print(first_lecturer < some_lecturer)
print(bad_student)
print(best_reviewer)
print(some_lecturer)
print(_average_grade([best_student, bad_student], 'Python'))
print(_average_grade([best_student, bad_student], 'Git'))
print(_average_grade_list([first_lecturer, some_lecturer]))