#COMBINING LIST & DICTIONARIES
#STUDENT REPORT CARD
import math
import numpy
students = [
    {"name":"john", "scores": [85,90,78]},
    {"name":"Mary", "scores": [92,88,95]},
    {"name":"Grace","scores": [70,75,80]}

]

students_0 = students[0] #position of the first element in the list
student_average = students_0["scores"]
student_name_0 = students_0["name"]
lenght = len(student_average)
sum = sum(student_average)
Average_0 = sum / lenght
print(f"{student_name_0}:  Average = {Average_0: .2f}")



students_1 = students[1] #position of the first element in the list
student_scores = students_1["scores"]
lenght_1 = len(student_scores)
student_name_1 = students_1["name"]
total = numpy.sum(student_scores)
Average_1 = total/lenght_1
print(f"{student_name_1}:  Average = {Average_1: .2f}")


student_2 = students[2]
student_scores_2 = student_2["scores"]
student_name_2 = student_2["name"]
lenght_2 = len(student_scores_2)
total_2 = numpy.sum(student_scores_2)
Average_2 = total_2 / lenght_2
print(f"{student_name_2}: Average = {Average_2: .2f}")


if Average_0 > Average_1 and Average_2:
    print(f"Top student: {student_name_0} with average: {Average_0: .2f}")

elif Average_1 > Average_0 and Average_2:
    print(f"Top student: {student_name_1} with average {Average_1: .2f}")


elif Average_2 > Average_0 and Average_1:
    print(f"Top student: {student_name_2} with average {Average_2}")

else:
    print(f"All student scored the same")


