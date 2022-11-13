class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grades(self):
        count = 0
        sum_grade = 0
        for value in self.grades.values():
            for elem in value:
                count += 1
                sum_grade += elem
        self.avg = sum_grade / count

    def __print_course(self):
        return ' '.join(self.courses_in_progress)

    def __print_finish_course(self):
        return ' '.join(self.finished_courses)

    def __str__(self):
        self.__avg_grades()
        res = f'Имя: {self.name}' + '\n' + \
              f'Фамилия: {self.surname}' + '\n' + \
              f'Средняя оценка за домашние: {self.avg}' + '\n' + \
              f'Курсы в процессе изучения: {self.__print_course()}' + '\n' + \
              f'Завершенные курсы: {self.__print_finish_course()}' + '\n'

        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        else:
            self.__avg_grades()
            return self.avg < other.avg


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}
        self.avg = 0

    def __avg_grades(self):
        count = 0
        sum_grade = 0
        for value in self.grades.values():
            for elem in value:
                count += 1
                sum_grade += elem
        self.avg = sum_grade / count

    def __str__(self):
        res = f'Имя: {self.name}' + '\n' + \
                f'Фамилия: {self.surname}' + '\n' + \
                f'Средняя оценка за лекции: {self.avg}' + '\n'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lucture')
            return
        else:
            self.__avg_grades()
            return self.avg < other.avg

            return self.avg


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
        res = f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}'
        return res


def avg_course_student(list_student, name_course):
    for elem in list_student:
        count = 0
        sum_elem = 0
        value_list = elem.grades[name_course]
        for value in value_list:
            count += 1
            sum_elem += value
        avg = sum_elem / count
        print(f'Студент {elem.name} {elem.surname} по курсу {name_course} имеет среднюю оценку {avg} ')
    return

def avg_course_lecture(list_lectures, name_course):
    for elem in list_lectures:
        count = 0
        sum_elem = 0
        value_list = elem.grades[name_course]
        for value in value_list:
            count += 1
            sum_elem += value
        avg = sum_elem / count
        print(f'Лектор {elem.name} {elem.surname} по курсу {name_course} имеет среднюю оценку {avg} ')
    return


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

second_student = Student("Gena", "Hardskill", "male")
second_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

lecturer = Lecturer("Rayan", "Gosling")
lecturer.courses_attached += ['Python']

second_lecturer = Lecturer("Dark", "Holm")
second_lecturer.courses_attached += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(second_student, 'Python', 8)
cool_mentor.rate_hw(second_student, 'Python', 8)
cool_mentor.rate_hw(second_student, 'Python', 8)

best_student.rate_hw(lecturer, 'Python', 9)
best_student.rate_hw(lecturer, 'Python', 9)
best_student.rate_hw(lecturer, 'Python', 9)

best_student.rate_hw(second_lecturer, 'Python', 8)
best_student.rate_hw(second_lecturer, 'Python', 8)
best_student.rate_hw(second_lecturer, 'Python', 8)

some_reviewer = Reviewer('Billy', 'Harington')

print(best_student.grades)
print(lecturer.grades)
print(best_student)
print(lecturer)
print(some_reviewer)
print(lecturer > second_lecturer)
print(best_student > second_student)

avg_course_student([best_student, second_student], 'Python')
avg_course_lecture([lecturer, second_lecturer], 'Python')