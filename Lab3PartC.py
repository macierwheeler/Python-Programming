# Creating a Student class. An object of type Student will be a record
# of information for a single student.
# The class should have three pieces of information: name, credit hours, and quality points.
# And your class should implement the following methods:
#   __init__(self, name, hours, qpoints)    A constructor creating student records with name, credit hours, and quality points.
#   getName(self)                           Return the student's name.
#   getHours(self)                          Return the student's credit hours.
#   getQPoints(self)                        Return the student's quality points.
#   gpa(self)                               Compute the student's GPA by dividing quality points by credit hours.
#
# Example:
# adams_henry = Student ("Adams Henry" , 127 , 228)
# adams_henry.getName() = "Adams Henry"
# adams_henry.getHours() = 127
# adams_henry.getQPoints() = 228
# adams_henry.gpa() = 1.795275590551181


class Student:
    ###
    def __init__(self,name, hours, qpoints):
        self.name = name
        self.hours = hours
        self.qpoints = qpoints

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours
    ###


adams_henry = Student ("Adams Henry", 127, 228)
print(adams_henry.getName())
print(adams_henry.getHours())
print(adams_henry.getQPoints())
print(adams_henry.gpa())
