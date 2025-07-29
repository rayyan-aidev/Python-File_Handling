import json
import csv
import os
print("This is the report generator.")
file_path1 = "File_Handling/Report_Generator/student_info.json"
file_path2 = "File_Handling/Report_Generator/student_marks.csv"
while True:

    student_marks = []
    print("To [E]xit")
    action = input("1-Register student\n2-Generate report\n")
    if action.lower().strip() == "e":
        break
    elif action.strip() == "1":
        if not os.path.exists(file_path1):
            with open(file_path1, "w") as file_json:
                json.dump({}, file_json)
        with open(file_path1, "r") as file_json:
            try:
                content_info = json.load(file_json)
            except Exception:
                content_info = {}
                with open(file_path1, "w") as file_json:
                    json.dump({}, file_json)
        name = input("Enter name of student: ").lower().strip()
        if name == "e":
            break
        section = input("Enter class and section of student: ")
        if section.lower().strip() == "e":
            break
        id = input("Enter the id of student:")
        if id.lower().strip() == "e":
            break
        marks = input(
            "Enter marks of students(seperated by commas)\nIn this order(Math, Urdu, English, Physics, Chemistry, Islamiat, Pst, CS)\n")
        if marks.lower().strip() == "e":
            break
        marks = marks.strip().replace(" ", "").split(",")
        if len(marks) != 8:
            print("Please enter correct number of marks.")
            continue
        if id in content_info:
            print("ID already registered")
            continue
        else:
            content_info[id] = {"Name": name.title(), "Section": section}
        with open(file_path1, "w") as file_json:
            json.dump(content_info, file_json,
                      indent=2, sort_keys=True)
        if not os.path.exists(file_path2):
            with open(file_path2, "w") as file_csv:
                fieldnames = ["ID", "Math", "Urdu", "English",
                              "Physics", "Chemistry", "Islamiat", "Pst", "CS"]
                writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
                writer.writeheader()
        with open(file_path2, "r") as file_csv:
            try:
                reader = csv.DictReader(file_csv)
                existing_data = list(reader)
                existing_data.append({"ID": id, "Math": marks[0], "Urdu": marks[1], "English": marks[2],
                                      "Physics": marks[3], "Chemistry": marks[4], "Islamiat": marks[5],
                                      "Pst": marks[6], "CS": marks[7]})
            except Exception:
                existing_data = []
        with open(file_path2, "w") as file_csv:
            fieldnames = ["ID", "Math", "Urdu", "English",
                          "Physics", "Chemistry", "Islamiat", "Pst", "CS"]
            writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
            if not os.path.exists(file_path2):
                with open(file_path2, "w") as file_csv:
                    writer = csv.DictWriter(
                        file_csv, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(existing_data)
            writer.writeheader()
            writer.writerows(existing_data)
    elif action.strip() == "2":
        report_number = input(
            "Generate report for\n1-One student\n2-All students\n")
        if report_number == "1":
            id = input("Enter student ID to generate report: ")
            if id.lower().strip() == "e":
                break
        elif report_number == "2":
            with open(file_path1, "r") as file_json:
                try:
                    content_info = json.load(file_json)
                except Exception:
                    content_info = {}
                ids = [student for student in content_info.keys()]
        else:
            print("Invalid option. Please try again.")
            continue
        if not os.path.exists(file_path1) or not os.path.exists(file_path2):
            print("No student information or marks registered yet.")
            continue
        with open(file_path1, "r") as file_json:
            try:
                content_info = json.load(file_json)
            except Exception:
                content_info = {}
        with open(file_path2, "r") as file_csv:
            try:
                reader = csv.DictReader(file_csv)
                existing_data = list(reader)
            except Exception:
                existing_data = []
        if not existing_data:
            print("No student marks registered yet.")
            continue
        if not os.path.exists("File_Handling/Report_Generator/Reports"):
            os.makedirs("File_Handling/Report_Generator/Reports")
        report_path = f"File_Handling/Report_Generator/Reports/{id}_report.txt"
        student_found = False
        if report_number == "1":
            if id not in content_info:
                print("Student ID not found.")
                continue
            for student in existing_data:
                if student["ID"] == id:
                    if id in content_info:
                        name = content_info[id]["Name"]
                        section = content_info[id]["Section"]
                        try:
                            average = sum(
                                float(student[subject]) for subject in student if subject != "ID") / 8
                        except Exception:
                            print("Error in marks data.")
                            continue
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
                        result = "Pass" if average >= 50 else "Fail"
                else:
                    continue
                with open(report_path, "w") as report_file:
                    report_file.write(
                        f"ID: {id}\nName: {name}\nSection: {section}\n")
                    report_file.write(
                        f"Marks:\n  Math: {student['Math']}\n  Urdu: {student['Urdu']}\n  English: {student['English']}\n  Physics: {student['Physics']}\n  Chemistry: {student['Chemistry']}\n  Islamiat: {student['Islamiat']}\n  Pst: {student['Pst']}\n  CS: {student['CS']}\n\n")
                    report_file.write(
                        f"Average: {average:.2f}\nGrade: {grade}\nResult: {result}\n\n")
                    print("Report generated successfully in reports folder.")
                student_found = True
                break
            if not student_found:
                print("Student ID not found.")
                continue
        elif report_number == "2":
            for id in ids:
                report_path = f"File_Handling/Report_Generator/Reports/{id}_report.txt"
                # Find the student marks for this id
                student = next(
                    (s for s in existing_data if s["ID"] == id), None)
                if student and id in content_info:
                    name = content_info[id]["Name"]
                    section = content_info[id]["Section"]
                    try:
                        average = sum(
                            float(student[subject]) for subject in student if subject != "ID") / 8
                    except Exception:
                        print(f"Error in marks data for ID {id}.")
                        continue
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
                    result = "Pass" if average >= 50 else "Fail"
                    with open(report_path, "w") as report_file:
                        report_file.write(
                            f"ID: {id}\nName: {name}\nSection: {section}\n")
                        report_file.write(
                            f"Marks:\n  Math: {student['Math']}\n  Urdu: {student['Urdu']}\n  English: {student['English']}\n  Physics: {student['Physics']}\n  Chemistry: {student['Chemistry']}\n  Islamiat: {student['Islamiat']}\n  Pst: {student['Pst']}\n  CS: {student['CS']}\n\n")
                        report_file.write(
                            f"Average: {average:.2f}\nGrade: {grade}\nResult: {result}\n\n")
            print(
                "Reports generated successfully in reports folder.")
    else:
        print("Invalid action. Please try again.")
