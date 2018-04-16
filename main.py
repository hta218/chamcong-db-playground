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


#
#
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
