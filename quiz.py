print("Welcome to our quiz app!")

print("Rules:" \
"1.Every letter should be written small." \
"2.The answer should be correct." \
"3.No cheating")

# Question 1
a = 1
quest1 = input("What is full name of CPU: ")
ans1 = "central processing unit"
while quest1 != ans1:
    print("Wrong answer. Try again. Point cut.")
    a = 0
    quest1 = input("What is full name of CPU: ")   
else:
    print("Good")
        
# Question 2
b = 1 
quest2 = input("What is the full form of RAM: ")
ans2 = "random access memory" 
while quest2 != ans2:
    print("Wrong answer. Try again. Point cut.")
    b = 0 
    quest2 = input("What is the full form of RAM: ")
else:
    print("good")
    
# Question 3
c = 1 
quest3 = input("What is the full form of ROM: ")
ans3 = "read only memory"    
while quest3 != ans3:
    print("Wrong answer. Try again. Point cut.")
    c = 0
    quest3 = input("What is the full form of ROM: ")
else:
    print("good")
    
# Question 4
d = 1 
quest4 = input("What is the full form of BIOS: ")
ans4 = "basic input output system"
while quest4 != ans4:
    print("Wrong answer. Try again. Point cut.")
    d = 0
    quest4 = input("What is the full form of BIOS: ")
else:
    print("good")

result = a + b + c + d
print(f"Final Score: {result}")
