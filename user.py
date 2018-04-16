from mongoengine import *

import mlab

mlab.connect()


class Instructor(Document):
    name = StringField()
    searchName = StringField()
    image = StringField()
    code = StringField()
    email = StringField()
    meta = {'collection': 'instructors', 'strict': False}


class User(Document):
    displayName = StringField()
    role = StringField()
    username = StringField()
    password = StringField()
    instructor = ObjectIdField()
    meta = {'collection': 'users', 'strict': False}

for (index, obj) in enumerate(Instructor.objects()):
    print("Saving user ", index + 1, end=', ')
    displayName = obj.name
    role = 'instructor'
    username = obj.email
    password = obj.email
    instructor = obj.id
    print("DisplayName: {0}, role: {1}, username: {2},\npassword: {3}, instructor id: {4}".format(displayName, role, username, password, instructor))
    user = User(displayName=displayName, role=role, username=username, password=password, instructor=instructor)
    user.save()
    print('Done\n')


