import pyexcel as p
from mongoengine import *
from utils import remove_accent
import mlab

mlab.connect()


# placeholder_image = "http://via.placeholder.com/400x200"
#

class Instructor(Document):
    name = StringField()
    searchName = StringField()
    image = StringField()
    code = StringField()
    email = StringField()
    meta = {'collection': 'instructors', 'strict': False}


#
#
records = p.iget_records(file_name="info.xlsx")
for index, record in enumerate(records):
    if record['Mã giảng viên'] == '':
        break

    name = record['Họ và tên']
    # image = "http://via.placeholder.com/400x200"
    code = record['Mã giảng viên']
    email = record['Email']
    # searchName = remove_accent(name).lower()

    # print(name)

    found_instructor = Instructor.objects(code=code)

    if found_instructor is not None:
       print("{2} - Found duplicates code={0}, name={1} updating ...".format(code, name, index + 1))
       found_instructor.update(set__email = email)
    else:
       # print("Saving: {0}, mail: {1}...".format(name, email), end="")
       # instructor = Instructor(name=name, image=image, searchName=searchName)
       # instructor.save()
       print("Found new instructor")
