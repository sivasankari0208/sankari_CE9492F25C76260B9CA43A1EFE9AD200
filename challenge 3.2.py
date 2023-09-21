class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  
  return sorted_students

students = [
  Student("Hari", "11", 7.8),
  Student("suji", "12", 8.9),
  Student("Jaswanth", "13", 9.1),
  Student("Dhakshika", "14", 9.9),
]

sort_students = sort_students(students)

for student in sort_students:
  print("Name: {}, Roll Nmuber: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))