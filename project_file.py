import time
class Student_Record:
    def __init__ (self,name) :
        self.name = name
        self.std_id = f"STD-{int(time.time())}"
        self.marks = {}

    def student_performance(self ,marks, subject):
        self.marks[subject] = marks

    def  print_details(self):
      print(f"Name : {self.name}")
      print(f"Student ID : {self.std_id}")

def main():
    Student_name = input("Enter Your Name : ")
    student = Student_Record(Student_name)

    conditon = True

    while conditon:

      subject = input(f"Enter subject for {Student_name} and 'S'for stop : ")
      if subject.lower() == "s":
        break

      try:
        marks = float(input(f"Input Marks for {subject} : "))

        if marks < 0 or marks > 100:
          while marks < 0 or marks > 100:
            print("Please enter a valid marks")
            marks = float(input(f"Input Marks for {subject} : "))
            student.student_performance(marks, subject)
          
        else :
          student.student_performance(marks, subject)
          print(student.marks)

      except ValueError:
        print("Please enter a valid marks")

    print("\n")
    student.print_details()

    for subject, marks in student.marks.items():
        print(f"{subject} : {marks}")
    try:
      average = sum(student.marks.values()) / len(student.marks)
      print(f"Average Marks : {average:.2f}")
      if average >= 85:
        print(f"{student.name} you Score a Excelent marks \"Well done {student.name}\"")
      elif average >=65 :
        print(f"{student.name} you Score a medium marks \"{student.name} Don't be Sad \"")
      elif average > 45 or average < 65:
        print(f"{student.name} you Score a weak marks \"{student.name} you need improvement\"")  
      elif average < 45:
        print(f"{student.name} you Score a Bad  marks \"{student.name} You need very hard work \"")
    
    except ZeroDivisionError:
      print("No subjects entered")
    

if __name__ == '__main__':
  main()
