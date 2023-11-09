#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

import random

class Student:
    def __init__(self, name, studentid, year, major, gpa):
        self.name = name
        self.studentid = studentid
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorseligible(self):
        if self.gpa > 3.5:

            print(self.name, "Is eligible for the honors program!")
            return True
        else:
            print(self.name, "Is not eligible for the honors program.")
            return False

    def freelunch(self):
        randomid = random.randint(1000, 9999)
        print(randomid)
        if self.studentid == randomid:
            print("Winner! student", self.name, "gets free lunch")
        else:
            print("Loser!")

    
    

    
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    student = Student("Chris", 6969, "Freshman", "Computer Science", 3.7)
    student.honorseligible()
    student.freelunch()
    
main()
