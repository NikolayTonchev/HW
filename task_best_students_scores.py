students_score = {
    'Ivan' : 5.00,
    'Alex' : 3.50,
    'Maria' : 5.50,
    'Georgy': 5.00
}

# Score greater than 4.00
best_students_score = {i: j for i, j in list(students_score.items()) if j > 4.0}

# Sort dictionary
best_students_score_sorted = dict(sorted(best_students_score.items(), key = lambda x: x[1], reverse=True))

# Print sorted results
for i, j in best_students_score_sorted.items():
    print(i + ' - ' + '{:.2f}'.format(j))


