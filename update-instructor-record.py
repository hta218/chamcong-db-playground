import pyexcel as p
from mongoengine import *
import re

import mlab

mlab.connect()

class InstructorRecord(Document):
    course = ObjectIdField()
    meta = {'collection': 'instructorrecords', 'strict': False}

class Course(Document):
    name = StringField()
    description = StringField()
    meta = {'collection': 'courses', 'strict': False}

def varify_course_id(course_name):
    course_id = None;
    for course_obj in Course.objects():
        if course_obj.id == course_name:
            course_id = course_obj.id

    return course_id


# for index, record in enumerate(InstructorRecord.objects()):
#     print(index + 1, end=' ')
#     course_name = record.course
#     course_id = varify_course_id(course_name)
#     if course_id is not None:
#         print(course_name, 'Checked')
#         # print(course_name, 'has id: ', course_id)
#         # print("Updating ", course_name, 'to: ', course_id)
#         # record.update(set__course=course_id)
#         # print('Done')
#         # print("*"*20)
#         # print("*"*20)
#     else:
#         print(course_name)
        # print('*'*50, 'Unknow course: ', course_name)


# TODO: update Intensive course, findout an "underfined" course
