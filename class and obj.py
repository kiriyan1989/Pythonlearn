# not all things can be covered by python data types.
# make our own data types.


#class is for a new data type
#we define our own data type using class

# eg. a student is not a data type in python
# we can make a new data type for student

from Student import Student # import Student.py file , then get Student class

from Student import graduate 

Learner1 = Student("Kiriyan", "Business", 3.1, False) # create an object called Learner1 from class Student
Learner2 = Student("Pam", "Art", 5.1, True)   #we assign values to class variables.

grad1 = graduate("eng", "Tony", "Art", 5.1, True)


#we make an instance variable called location for Learner1 object.
Learner1.location = "Glasgow"


print(grad1.job)

print(Learner1.name)

print(Learner1.location)

#print all the variables associated with the object Learner1
print(Learner1.__dict__)

"""
print(Learner1.name)
print(Learner2.is_on_probation)

print(Learner2.on_honor_roll())

print(Learner1.name)
"""


"""
import Student from student
student1 = student ("kiriyan","business", 3.1, False)

print(student1.name)
"""