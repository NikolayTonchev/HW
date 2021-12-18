students_score = {
    'Ivan' : 5.00,
    'Alex' : 3.50,
    'Maria' : 5.50,
    'Georgy': 5.00
}

# Get max score
max_student_score = {i: j for i, j in list(students_score.items()) if j == max(students_score.values())}

# Get min score
min_student_score = {i: j for i, j in list(students_score.items()) if j == min(students_score.values())}

# Print max score 
for i, j in max_student_score.items():
    print(i + ' - ' + '{:.2f}'.format(j))

# Print min score
for i, j in min_student_score.items():
    print(i + ' - ' + '{:.2f}'.format(j))