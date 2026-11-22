import pickle

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


def save_object(obj):
    with open("student.dat", "wb") as file:
        pickle.dump(obj, file)
    print("Object serialized successfully!")


def load_object():
    with open("student.dat", "rb") as file:
        obj = pickle.load(file)
    print("Object deserialized successfully!")
    return obj


name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = Student(name, roll, marks)

save_object(student)

restored_student = load_object()

print("\nRestored Student Details:")
restored_student.display()
