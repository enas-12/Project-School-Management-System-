#to Recall the intialization data from Student file 
from students import Student

#to add the feature and authorization for Manager 
class Manager:
    def __init__(self):
        self.student = []
        
#to Add new student "Manual insertion"
def add (self, Name, Gender, Grade,Student_class, Age):
    New_student = Student(Name, Gender, Grade,Student_class, Age)
    self.student.append(New_student)
    return New_student 


#to add function of Searching with ID & Name 
def Find(self,uuid,name):
   for Student in self.student:       
       if name.lower() == self.Student():
        return self.student()
       elif uuid == self.Student():
        return self.student()
       return  "No Student is exist"

#to Remove Student according the search i got    
def Remove(self):
    if self.Find.uuid == self.Student.ID:
        self.Student.remove()
        return "{self.name} had been Removed"
    return None
    




