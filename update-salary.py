import pyexcel as p
from mongoengine import *
import re

import mlab

mlab.connect()

class Salary(Document):
    instructor = StringField()
    course = ObjectIdField()
    role = StringField()
    salary = DecimalField()
    meta = {'collection': 'salary', 'strict': False}

class Course(Document):
    name = StringField()
    description = StringField()
    meta = {'collection': 'courses', 'strict': False}


def get_course_id(course):
    course_id = None;
    for course_obj in Course.objects():
        if course_obj.name == course:
            course_id = course_obj.id

    return course_id

for salary in Salary.objects():
    course_name = salary.course
    course_id = get_course_id(course_name)
    if course_id is not None:
        print("Updating ", course_name, 'to: ', course_id)
        salary.update(set__course=course_id)
        print('Done')
        print("*"*20)
        print("*"*20)
    else:
        print('*******************Unknow course: ', course_name)
