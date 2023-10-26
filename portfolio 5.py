students_list = [113, 175, 12]
for students in students_list:
    full_groups = students // 24
    remaining_students = students % 24
    print(f"For {students} students, you will need {full_groups} full groups and {remaining_students} students in the left over group.")
