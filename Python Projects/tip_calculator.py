print("Welcome to tip calculator!")
bill = float(input("What's the total bill: "))
tip = int(input("How much percent tip you want to give?: "))
people = int(input("Among how many people to split the bill: "))
each_person_bill = (bill + (tip/100) * bill)/people
print(f"Each Person Share is ${each_person_bill}")