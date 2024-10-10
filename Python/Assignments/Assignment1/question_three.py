#Question One
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 



def student_grade():
     student_name = str(input('Enter student\'s name: '))
     student_score = float(input("Enter student's grade: "))
     if student_score>=90:
          print(f'{student_name}\'s Grade is A')
     elif student_score >=80:
          print(f'{student_name}\'s Grade is B')
     elif student_score >=70:
          print(f'{student_name}\'s Grade is C')
     elif student_score >=60:
          print(f'{student_name}\'s Grade is C')
     elif student_score >=50:
          print(f'{student_name}\'sGrade is D')
     else:
          print(f'{student_name}\'s Grade is Fail')

student_grade()