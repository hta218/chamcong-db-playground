import pyexcel as p
from mongoengine import *
import re

import mlab

mlab.connect()

def remove_accent(s):
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(u'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(u'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(u'[ìíịỉĩ]', 'i', s)
    s = re.sub(u'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(u'[ùúùụủũưừứựửữ]', 'u', s)
    s = re.sub(u'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(u'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(u'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(u'[Đ]', 'D', s)
    s = re.sub(u'[đ]', 'd', s)
    return s

class InstructorRecord(Document):
    instructor = ObjectIdField()
    course = ObjectIdField()
    role = StringField()
    meta = {'collection': 'instructorrecords', 'strict': False}

class Salary(Document):
    instructor = StringField()
    course = ObjectIdField()
    role = StringField()
    salary = DecimalField()
    meta = {'collection': 'salary', 'strict': False}

class Instructor(Document):
    code = StringField()
    meta = {'collection': 'instructors', 'strict': False}


def get_salary(instructor_code, course_id):
    salary = Salary.objects(instructor=instructor_code, course=course_id)
    return salary

def get_instructor_code(instructor_id):
    code = None
    found_instructor = Instructor.objects().with_id(instructor_id)

    if found_instructor:
        return found_instructor.code

    return code

for index, record in enumerate(InstructorRecord.objects()):
    
    print('Record', index + 1, end=' ')

    instructor_code = get_instructor_code(record.instructor)

    salary = get_salary(instructor_code, record.course)

    if salary:
        print('Salary already exist with id: ', salary[0].id)
    else:
        print('Saving new salary document ... ')
        new_salary = Salary(instructor=instructor_code, course=record.course, role=record.role, salary=15000)
        new_salary.save()
