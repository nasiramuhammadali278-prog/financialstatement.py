name = input("Enter student name:")

marks_1 = int(input("Enter student math/75 marks:"))
marks_2 = int(input("Enter student physics/75 marks:"))
marks_3 = int(input("Enter student english/75 marks:"))
if marks_1 > 75:
        print("total marks are 75")
elif marks_2 > 75:
        print("total marks are 75")
elif marks_3 > 75:
        print("total marks are 75")

average = (marks_1 + marks_2 + marks_3) / 3

print(average)

if average > 70:
    print("Excellent! Nice work keep it up.")
elif average > 60:
    print("Very satisfied!")
elif average > 50:
    print("Satisfied.")
elif average > 40:
    print("Very good, keep pushing.")
elif average >= 30:
    print("Passed, but needs a lot of improvement.")
else:
    print("Sorry, you have failed.")
     
print(f"{name} your average is {average}")