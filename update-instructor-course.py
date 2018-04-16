from mongoengine import *

import mlab

mlab.connect()

class Course(Document):
    name = StringField()
    description = StringField()
    isActive = BooleanField()
    meta = {'collection': 'courses', 'strict': False}

class Instructor(Document):
    name = StringField()
    code = StringField()
    courses = ListField()
    meta = {'collection': 'instructors', 'strict': False}

class Salary(Document):
    instructor = StringField()
    course = ObjectIdField()
    role = StringField()
    salary = DecimalField()
    meta = {'collection': 'salary', 'strict': False}

def get_all_instructor_course(instructor_code):
    instructor_courses = []
    for salary in Salary.objects(instructor=instructor_code):
        if salary.course not in instructor_courses:
            instructor_courses.append(salary.course)
    return instructor_courses

for instructor in Instructor.objects():
    print('Update', instructor.name, '. Courses: ', end=' ')
    courses = get_all_instructor_course(instructor.code)
    print(courses)
    instructor.update(set__courses=courses)
