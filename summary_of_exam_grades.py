#🇵🇱 Uczniowie klasy 1A pisali egzamin z angielskiego. Wyniki są w słowniku exam_points. Przygotuj listę uczniów, którzy
# nie zdali (failed_students), listę tych z oceną bardzo dobrą (top_students) oraz krotkę z najlepszym uczniem
# i jego wynikiem (best_student).

#🇬🇧 The students in Class 1A took an English exam. The results are stored in the `exam_points` dictionary. Prepare a list
# of students who failed (`failed_students`), a list of those with a “very good” grade (`top_students`), and
# a tuple containing the top student and their score (`best_student`).

exam_points = {"Mariusz":30, "Mateusz":55, "Marta":76, "Roman":30,
"Arleta":59, "Adrian":96, "Monika":91, "Andrzej":22,
"Krzysztof":83, "Krystyna":93, "Piotr":44, "Dawid":10, "Agnieszka":15}
# skala: 0-45 ndst | 46-60 dop | 61-75 dst | 76-90 db | 91-100 bdb
# grading scale: 0–45: failing | 46–60: passing | 61–75: good | 76–90: very good | 91–100: excellent

failed_students = []
top_students = []
grades = []

for name, score in exam_points.items():
    if score <= 45:
        failed_students.append(name)
    if score >= 91:
        top_students.append(name)
    grades.append(score)

print(f"Failed students: {failed_students}")
print(f"Top students: {top_students}")
best_grade = max(grades)

for name, score in exam_points.items():
    if score >= best_grade:
        best_student = (name, score)
        print(f"Best student: {best_student}")



