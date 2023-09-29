
def main():

    #that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
    #enter your name here
    name = "Chris"
    '''in this if/elif/else, add 4 mispellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name" '''
    if name == "Crud":
        print("That's not right!")
    elif name == "Kris":
        print("That's not right!")
    elif name == "Cris":
        print("That's not right!")
    elif name == "Chris":
        print("That's right!")
    else:
        print("You cant spell!")
    #etc etc, the else can be whatever you want
    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = input("Enter a number to find out if its even or odd: ")
    even = int(even)
    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print("Even")
    else:
        print("Odd")
  
  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why? - went up one on the list
    numbers = [1,2,3,4,5]
    print(numbers[1])
    print(numbers[3])
    print(numbers[3] / numbers[1])
    print(numbers[3] * numbers[1])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[1])
    print(numbers2[4])
    
    #Here's a fun one: This is a list of everyone's name. Find where yours is and print the index of your name
    students = ["Tobi","Brad","Tiff","Oscar","Tommy","Kyra","Matt C","Morgan","Haley","Matt F","Sydney","Pedro","Nathan","Bryce","Chris","Iram","Pat","Maddie","Daniel","Tomas","Gabriella","Ben","Lucian","Dean","Jack","Natalie","Athina"]
    print(students[14])
main()
    
    

    
