# 1.Smart Home Light System

time = input("Enter time (morning/evening/night): ").lower()
presence = input("Is someone in the room? (yes/no): ").lower()

if time == "morning":
    print("Lights OFF")
elif time == "evening":
    if presence == "yes":
        print("Lights ON")
    else:
        print("Lights OFF")
elif time == "night":
    if presence == "yes":
        print("Lights in DIM Mode")
    else:
        print("Security Mode Activated")



# 2.E-commerce Shipping Policy

amount = int(input("Enter order amount: "))
member = input("Membership (Prime/Regular): ").lower()

if amount >= 1000:
    print("Free Shipping")
else:
    if member == "prime":
        print("Free Shipping (Prime Benefit)")
    else:
        print("Delivery charges applied")



# 3. Online Exam Eligibility

attendance = int(input("Enter attendance %: "))
internal = int(input("Enter internal marks: "))

if attendance >= 75:
    if internal >= 25:
        print("Eligible for Exam")
    else:
        print("Not eligible - Internal marks too low")
else:
    print("Not eligible - Attendance shortage")



# 4.Bus Fare Discount

age = int(input("Enter age: "))

if age < 12:
    print("Free ride")
else:
    if age <= 60:
        print("Normal fare")
    else:
        print("Senior citizen discount")
