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
    meta = {'collection': 'instructorrecords', 'strict': False}

class Salary(Document):
    instructor = ObjectIdField()
    course = ObjectIdField()
    role = StringField()
    salary = DecimalField()
    meta = {'collection': 'salary', 'strict': False}

# instructor_info = {}
# instructors = p.iget_records(file_name="info.xlsx")
# for instructor in instructors:
#     if instructor['Họ và tên'] == '':
#         break
#
#     name = instructor['Họ và tên']
#     searchName = remove_accent(name).lower()
#     code = instructor['Mã giảng viên']
#
#     instructor_info[searchName] = code
#
# records = p.iget_records(file_name="salary.xlsx")

for record in records:
    if record['Họ và tên'] == '':
        break

    name = record['Họ và tên']
    searchName = remove_accent(name).lower()
    course = record['Khóa học']
    instructorSalary = record['Mức lương GV']
    coachSalary = record['Mức lương trợ giảng']
    if instructorSalary == "":
        instructorSalary = 0
    if coachSalary == "":
        coachSalary = 0

    if searchName != 'nguyen thanh tung':
        print("Saving.... Giang vien: {0}, Course: {1}, role: instructor, salary: {2}".format(
            instructor_info[searchName], course, instructorSalary))
        instructorSalary = Salary(instructor=instructor_info[searchName], course=course, role='instructor', salary=instructorSalary)
        instructorSalary.save()
        print("Done")

        print("Saving.... Giang vien: {0}, Course: {1}, role: coach, salary: {2}".format(instructor_info[searchName], course, coachSalary))

        coachSalary = Salary(instructor=instructor_info[searchName], course=course, role='coach', alary=coachSalary)
        coachSalary.save()
        print("Done")
    else:
        print(searchName)
##    found_instructor = Instructor.objects(searchName=searchName).first()
##
##    if found_instructor is not None:
##        print("Found duplicates searchName={0}, updating ...".format(searchName))
##        found_instructor.update(set__code = code)
##    else:
##        print("Saving {0}...".format(name), end="")
##        instructor = Instructor(name=name, image=image, searchName=searchName)
##        instructor.save()
##        print("Done")
