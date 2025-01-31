import random
one = """ 
            ("===========")
            ("|         |")
            ("|    O    |")
            ("|         |")
            ("===========")\n  

        """
two = """ 
            ("===========")
            ("|         |")
            ("| O     O |")
            ("|         |")
            ("===========")\n  

        """
three = """ 
            ("===========")
            ("|    O    |")
            ("|    O    |")
            ("|    O    |")
            ("===========")\n  

        """
four = """ 
            ("===========")
            ("|  O    O |")
            ("|     0   |")
            ("|  O    O |")
            ("===========")\n  

        """
five = """ 
            ("===========")
            ("| O     O |")
            ("|    0    |")
            ("| O     O |")
            ("===========")\n  

        """
six = """
            ("===========") 
            ("| O     O |")
            ("| O     O |")
            ("| O     O |")
            ("===========") \n      
        """
l = [one, two, three, four, five, six]

print("This is a dice stimulator")
x = "yes"
while x == "yes":
    output = random.sample(l, 2)
    for i in output:
        print(i)
    x = input("Type 'yes' to roll again: ")