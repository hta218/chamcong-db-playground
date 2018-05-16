from mongoengine import *

class Instructor(Document):
  name=StringField()
  firstName=StringField()
  lastName=StringField()
  meta = {
    "collection": "instructors",
    "strict": False
  }

  def print(self):
    print("{0} {1} {2}".format(self.name, self.lastName, self.firstName))

def separateName():
  for instructor in Instructor.objects():
    # instructor.print()
    if instructor.name and not instructor.firstName:
      # instructor.print()
      name_parts = instructor.name.split(" ")
      # print(name_parts)
      if len(name_parts) > 1:
        firstName = name_parts[-1]
        name_parts.pop(-1)
        lastName = " ".join(name_parts)
        instructor.update(set__firstName=firstName, set__lastName=lastName)
        instructor.reload()
        instructor.print()
    # break