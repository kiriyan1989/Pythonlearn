class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):     
        # __init__ is class initialize  function 
        # self refers to the actual object.
        
        # we define the attributes below
        self.name = name #name for student
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


    ########class function########
    ## custom function within the object to be made using class Student.
    # this function can be used by this object 
    # (a custom method for the object , once object is made)

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class graduate(Student):
    def __init__(self, job):    
        self.job = job