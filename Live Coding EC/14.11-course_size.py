class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa


class Course:
    def __init__(self):
        self.course_roster = []

    def add_student(self, student):
        self.course_roster.append(student)

    def course_size(self):
        return len(self.course_roster)


if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Bendel', 3.6))
    course.add_student(Student('Johnny', 'Moin', 2.9))

    print('Course size:',course.course_size())