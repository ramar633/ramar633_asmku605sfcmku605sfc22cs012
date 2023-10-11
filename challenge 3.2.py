class student:
  def__init__(self,name,roll_number,cgpa):
    self.name=Name
  self.roll_number=roll_number
  self.cgpa=cgpa
  def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=true)
    return sorted_students
    #example usuage:
    student1=student("alice","s123",3.7)
    student2=student("bob","s124",3.9)
    student3=student("charlie","s125",3.5)
    student4=student("david","s126",3.8)
    students=[student1,student2,student3,student4]
    sorted_students=sort_students(students)
    #print the sorted list of students by CGPA in descending order 
    for student in sorted_students:
      print(f"name:{student.name},roll number:{student.roll_number},CGPA:{student.cgpa})