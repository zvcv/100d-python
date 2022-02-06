# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_heights = 0
for x in student_heights:
    total_heights += x

total_students = 0
for y in student_heights:
    total_students += 1

average = round(int(total_heights / total_students))

print (f"the average student height is {average}")

# much easier way 👇 tapi gaboleh pake ini karena lagi belajar loop

# total_heights = sum(student_heights)
# total_students = len(student_heights)
# average_height = round(total_heights/total_students)

# print (f"the average student height is {average_height}")