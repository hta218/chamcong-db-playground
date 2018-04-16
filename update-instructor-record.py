import pyexcel as p
from mongoengine import *
import re

import mlab

mlab.connect()


class InstructorRecord(Document):
    course = ObjectIdField()
    className = StringField()
    classNo = IntField()
    meta = {'collection': 'instructorrecords', 'strict': False}


class Course(Document):
    name = StringField()
    description = StringField()
    meta = {'collection': 'courses', 'strict': False}


def varify_course_id(course_name):
    course_id = None
    for course_obj in Course.objects():
        if course_obj.id == course_name:
            course_id = course_obj.id

    return course_id



def convert_class_no():
    phrase_to_remove = ["1.100", "F", "GRE", "1.", "2.", "3."]
    with open("record_class_no.log", "w") as f:
        for record in InstructorRecord.objects():
            className = record.className
            if className is None or className == "":
                f.write(str(record.id) + "\n")
            else:
                splittedClassName = record.className.split(" ")
                lastStringInClassName = splittedClassName[-1]
                if len(splittedClassName) == 0:
                    f.write(str(record.id) + "\n")
                else:
                    for p in phrase_to_remove:
                        lastStringInClassName = lastStringInClassName.replace(p, "")
                    if lastStringInClassName == "":
                        f.write(str(record.id) + "\n")
                    else:
                        print("Trying to convert ...")
                        class_no = int(lastStringInClassName)
                        print(class_no)
                        record.update(set__classNo=class_no)
                        record.reload()
                        if record.classNo == class_no:
                            print("Updated successfully")
                        else:
                            print("Did not work")
                        #f.write(lastStringInClassName + "\n")


if __name__ == "__main__":
    convert_class_no()
