# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0

for x in student_heights: 
    total_height+=x

print(round(total_height/(len(student_heights))))


# Or even more challenging

total_height = 0
total_students = 0

for x in student_heights: 
   total_height+=x
   total_students+=1

print(round(total_height/total_students))

print(round(sum(student_heights)/len(student_heights)))