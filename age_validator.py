
print("Welcome to Summer Camp Registration 2026") 

print("The camp is divided into three age groups:")
print("1. Ages 6-10 (kids)")
print("2. Ages 11-15 (teens)")
print("3. Ages 16-20 (youth)")

age = input("Please enter the age of the camper: ")

if age.isdigit():
    age = int(age)
    if age == 0:
          print("Nice one, but please enter a valid age.")
    else:
        if 6 <= age <= 10:
                print("The camper will be placed in the Kids group.")
        elif 11 <= age <= 15:
                print("The camper will be placed in the Teens group.")
        elif 16 <= age <= 20:
                print("The camper will be placed in the Youth group.")
        else:
                print("Sorry, the age entered does not fall within the eligible age for summer camp 2026.")
else:
    print("Invalid input. Please enter an age in form of a number.")


