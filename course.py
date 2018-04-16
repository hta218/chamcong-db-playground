from mongoengine import *

import mlab

mlab.connect()

class Course(Document):
    name = StringField()
    description = StringField()
    isActive = BooleanField()
    meta = {'collection': 'courses', 'strict': False}

courses = [
      {'name': "Android", 'description': "Android"},
      {'name': "C4E", 'description': "C4E"},
      {'name': "C4K", 'description': "C4K"},
      {'name': "C4K Advance", 'description': "C4K Advance"},
      {'name': "C4K F", 'description': "C4K F"},
      {'name': "CFA 1", 'description': "CFA 1"},
      {'name': "CFA 2", 'description': "CFA 2"},
      {'name': "CI", 'description': "CI"},
      {'name': "Foundation", 'description': "Foundation"},
      {'name': "Game", 'description': "Game"},
      {'name': "GMAT", 'description': "GMAT"},
      {'name': "GRE", 'description': "GRE"},
      {'name': "IELTS Intensive", 'description': "IELTS Intensive"},
      {'name': "IELTS Advance", 'description': "IELTS Advance"},
      {'name': "IELTS L&R Advance", 'description': "IELTS L&R Advance"},
      {'name': "IELTS S Advance", 'description': "IELTS S Advance"},
      {'name': "IELTS Pre-Inter", 'description': "IELTS Pre-Inter"},
      {'name': "IELTS L&R Pre-Inter", 'description': "IELTS L&R Pre-Inter"},
      {'name': "IELTS S Pre-Inter", 'description': "IELTS S Pre-Inter"},
      {'name': "IELTS Inter", 'description': "IELTS Inter"},
      {'name': "IELTS L&R Inter", 'description': "IELTS L&R Inter"},
      {'name': "IELTS S Inter", 'description': "IELTS S Inter"},
      {'name': "iOS", 'description': "iOS"},
      {'name': "Pronunciation", 'description': "Pronunciation"},
      {'name': "Web", 'description': "Web"}
];


for (index, course_iterator) in enumerate(courses):
    print("Saving course ", index + 1, end=', ')

    name = course_iterator['name']
    description = course_iterator['description']
    isActive = True

    print("Name: {0} ".format(name))
    course = Course(name=name, description=description, isActive=isActive)
    course.save()
    print('Done\n')
