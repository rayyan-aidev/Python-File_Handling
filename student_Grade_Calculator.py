def grade_calculator():
    print("This is the Grade calculator.")
    while True:
        print("To [E]xit")
        subject_amount = input("Enter amount of subjects taken: ")
        if subject_amount.lower() == "e":
            break
        subject_amount = int(subject_amount)
        subjects = input("Enter the subjects(comma_seperated): ").strip()
        if subjects.lower() == "e":
            break
        subjects = subjects.replace(" ", "").split(",")
        subjects_capatallized = []
        for subject in subjects:
            subject = subject.capitalize()
            subjects_capatallized.append(subject)
        subject_marks = []
        for i in range(len(subjects)):
            marks = input(f"Enter marks of {subjects_capatallized[i]}: ")
            if marks.lower == "e":
                break
            marks = float(marks)
            subject_marks.append(marks)
        total_marks = 100 * subject_amount
        total_marks_obtained = sum(subject_marks)
        average = total_marks_obtained / subject_amount
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "U"
        if average >= 50:
            result = "Pass"
        else:
            result = "Fail"
        print(
            f"\nYou have got {total_marks_obtained} marks out of {total_marks} marks.\nYour average is {average}.\nYour grade is {grade}.\nResult: {result}.")
    print("Grade Calculator exited.")


grade_calculator()
