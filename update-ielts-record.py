from mongoengine import *
from bson import ObjectId
from datetime import *
from time import *

import mlab
import re

mlab.connect()

class Instructor(Document):
    name = StringField()
    code = StringField()
    courses = ListField()
    meta = {'collection': 'instructors', 'strict': False}

class Course(Document):
    name = StringField()
    meta = {'collection': 'courses', 'strict': False}
    

class InstructorRecord(Document):
    instructor = ReferenceField("Instructor")
    course = ReferenceField("Course")
    className = StringField()
    role = StringField()
    recordDate = DateTimeField()
    addedDate = DateTimeField()
    meta = {'collection': 'instructorrecords', 'strict': False}

courses = {
        "c4kf" : "C4K F",
        "c4k" : "C4K",
        "android" : "Android",
        "c4e" : "C4E",
        "ci" : "CI",
        "cfa1" : "CFA 1",
        "cfa2" : "CFA 2",
        "game" : "Game",
        "pre" : "IELTS",
        "adv" : "IELTS",
        "advance" : "IELTS",
        "inter" : "IELTS",
        "pro" : "Pronunciation",
        "gmat" : "GMAT",
        "gre" : "GRE",
        "ios" : "iOS",
        "found" : "Foundation",
        "web" : "Web",
        "it" : "IT"
    }

pre_names = {
    "adv" : " Advance ",
    "pre" : " Pre-Inter ",
    "inter" : " Inter ",
    "cfa" : ".",
    "c4kf" : ""
}


def remove_symbol(className):
    className = className.replace('.', ' ')
    className = className.replace('_', ' ')
    className = className.replace('-', ' ')
    className = className.replace(' ', '')

    return className


def get_class_name(old_course, new_course, className):
    pre_name = ' '
    class_no = ''

    class_nos = re.findall('\d+', className.replace(old_course, ''))
    if class_nos:
        class_no = class_nos[0]

    for (key, value) in pre_names.items():
        if key in className:
            pre_name = pre_names[key]

    return new_course + pre_name + class_no


def update_class_name(className):
    className = remove_symbol(className).lower()

    course = "Undefined"
    class_name_updated = className

    for old_course in courses.keys():
        if old_course in className:
            course = courses[old_course]
            class_name_updated = get_class_name(old_course, course, className)
            break

    return course, class_name_updated


def update_class_number(className):
    className = className.replace('0', '')
    return className


# for updating IELTS records
records = []

count = 1

for (index, record) in enumerate(InstructorRecord.objects(className__contains="IELTS", recordDate__gte=datetime(2018, 2, 28))):
    # IELTS: 5a93e08bce45bc0004ff5fb5   # Foundation: 5a3b785297b65c0fa06c8b49
    ielts_record = {}
    ielts_record['ID(Không được sửa cột này)'] = str(record.id)
    ielts_record['Ngày'] = record.recordDate.strftime('%d/%m/%Y')
    # ielts_record['Giờ ghi nhận chấm công'] = record.recordDate.strftime('%H:%M')
    ielts_record['Giảng-viên'] = record.instructor.name
    ielts_record['Khóa-học'] = record.course.name
    ielts_record['Lớp'] = record.className
    # print(count, ielts_record)
    records.append(ielts_record)
    count += 1

sorted_records = sorted(records, key=lambda k: k['Giảng-viên'])

import pyexcel

pyexcel.save_as(records=sorted_records, dest_file_name="IELTS.xlsx")