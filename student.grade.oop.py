import numpy as np


all_data = {}

class Student: 
    def __init__(self):
        self.name = input("Please input your name: ")
        self.clas = int(input("Please input your class (1-12): "))
        
       
        if not (1 <= self.clas <= 12):
            print("Invalid class! Defaulting to 1.")
            self.clas = 1
            
        self.eng = int(input("English /75: "))
        self.math = int(input("Math /75: "))
        self.phy = int(input("Physics /75: "))
        
        self.total = self.eng + self.math + self.phy
        
       
        all_data[self.name] = {
            "class": self.clas,
            "marks": [self.eng, self.math, self.phy],
            "total": self.total
        }

    def display(self):
        print(f"\n--- Report for {self.name} ---")
        print(f"Total: {self.total}/225")


while True:
    s = Student()
    s.display()
    if input("\nAdd another? (y/n): ").lower() != 'y':
        break

print("\n--- Final Analytics ---")

totals = [data["total"] for data in all_data.values()]
avg_score = np.mean(totals)

print(f"Total Students: {len(all_data)}")
print(f"Class Average: {avg_score:.2f}")