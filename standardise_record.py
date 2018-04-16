from mongoengine import *

import mlab
import re

mlab.connect()


class InstructorRecord(Document):
    instructor = StringField()
    course = StringField()
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

for (index, record) in enumerate(InstructorRecord.objects(className__contains='0')):
    if "10" not in record.className and "20" not in record.className:
        print("Record ", index + 1, end=', ')

        ################# update class name + course
        # course, class_name_updated = update_class_name(record.className)
        #
        # print('Updating Class name: ', record.className,)
        # print("\t\tCourse: {0},\n\t\tClass name updated: {1}".format(course, class_name_updated))
        #
        # record.update(set__course = course, set__className = class_name_updated)
        #######################################

        ################ update class number

        class_name_updated = update_class_number(record.className)

        print('Updating Class name: ', record.className,)
        print("\t\tClass name updated: {0}".format(class_name_updated))

        record.update(set__className = class_name_updated)
        ########################

        print("\t\tDONE !!!")

