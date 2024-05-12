grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_students = sorted(students)      # Сортировка множества по алфавиту
dict_students = {}

for i in range(len(grades)):
    average_score = sum(grades[i])/len(grades[i])
    print(average_score, type(average_score))
    print(dict_students)
    dict_students.update({sort_students[i]: average_score})


print("Словарь  со средним баллом студентов:")
print(dict_students)


