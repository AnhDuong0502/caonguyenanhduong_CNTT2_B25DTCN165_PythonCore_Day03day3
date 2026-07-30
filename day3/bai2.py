students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4},
]


def bubble_sort_students(students):
    n = len(students)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if students[j]["gpa"] < students[j + 1]["gpa"]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True

        if not swapped:
            break

    return students


sorted_students = bubble_sort_students(students.copy())

print("BẢNG XẾP HẠNG SINH VIÊN (BUBBLE SORT - GPA GIẢM DẦN)")

for i, student in enumerate(sorted_students, start=1):
    print(f"Top {i}: {student['name']} - {student['gpa']} điểm")
