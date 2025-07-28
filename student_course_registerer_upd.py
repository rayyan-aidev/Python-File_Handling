print("This is the student portal.\nTo [E]xit.")
student_info = {

}


def take_info():
    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            id = input("Enter your ID number: ")
            courses = input("Enter the courses(comma-spearated): ")
            courses = set(courses.strip().replace(
                " ", "").title().split(","))
            return name, age, id, courses
        except ValueError:
            print("Please enter correct info type.")


file_path = "Beginner useful/student_info.txt"

while True:
    print("To [E]xit.")
    try:
        action = input(
            "\nWhat do you want to do? \n1-Register\n2-Unregister\n3-View\n ")
        if action.lower() == "e":
            break

        elif action == "1":
            name, age, id, courses = take_info()
            personal_info = {"Name: ": name.title(), "Age:": age}
            number_of_courses = len(courses)
            with open(file_path, "a+") as f:
                f.seek(0)
                all_info = f.read()
                if id in all_info:
                    print("ID already registered.")
                else:
                    student_info[id] = {
                        "Personal Info:": personal_info,
                        "Courses": f"{courses}-",
                        "Number of Courses": number_of_courses
                    }
                    print(f"Student {name.title()} registered succesfully.\n")
                    str_id = f"{id}:{student_info[id]}"
                    f.write(str_id + "\n")

        elif action == "2":
            unregister = input(
                "1-From whole database\n2-Specific courses\n3-All courses\n ")
            if unregister.lower().strip() == "e":
                break
            if unregister == "1":
                id = input("Enter your ID number: ")
                if id.lower().strip() == "e":
                    break
                with open(file_path, "r") as f:
                    all_info = f.read()
                    if id in all_info:
                        f.seek(0)
                        all_info_list = f.readlines()
                        for info in all_info_list:
                            if id in info:
                                all_info_list.remove(info)
                        if not (id in all_info_list):
                            with open(file_path, "w") as f:
                                for info in all_info_list:
                                    f.write(info)
                            print(
                                f"ID:{id} unregistered completely from database.")
                    else:
                        print("ID not registered")
            elif unregister == "2":
                id = input("Enter your ID number: ")
                if id.lower().strip() == "e":
                    break
                with open(file_path, "r") as f:
                    all_info_list = f.readlines()
                found = False
                for idx, info in enumerate(all_info_list):
                    # This assumes id is before the first colon
                    if info.strip().startswith(f"{id}:"):
                        found = True
                        # Extract courses part
                        try:
                            # Find the part like "'Courses': {...}-"
                            course_start = info.find("'Courses':")
                            if course_start == -1:
                                print("No courses found for this student.")
                                break
                            course_end = info.find("-", course_start)
                            # Extract and clean up the courses set as a string
                            course_set_str = info[course_start +
                                                  10:course_end].strip()
                            course_set_str = course_set_str.strip("{} ")
                            current_courses = set(
                                c.strip().strip("'") for c in course_set_str.split(",") if c.strip() and c.strip() != "''"
                            )
                            # Ask which to remove
                            courses_to_remove = input("Which courses: ")
                            if courses_to_remove.lower().strip() == "e":
                                break
                            remove_set = set(
                                c.strip().title() for c in courses_to_remove.replace(" ", "").split(",") if c.strip()
                            )
                            updated_courses = current_courses - remove_set
                            new_courses_str = + ", ".join(
                                f"'{c}'" for c in sorted(updated_courses))
                            # Replace only the courses part in the line
                            new_info = info[:course_start + 10] + \
                                new_courses_str + info[course_end:]
                            all_info_list[idx] = new_info
                            with open(file_path, "w") as f:
                                f.writelines(all_info_list)
                            print(
                                f"Courses {', '.join(remove_set)} unregistered from ID {id}.")
                        except Exception as e:
                            print("Error processing courses:", e)
                        break
                if not found:
                    print("ID does not exist.")
            elif unregister == "3":
                id = input("Enter your ID number: ")
                if id.lower().strip() == "e":
                    break
                with open(file_path, "r") as f:
                    all_info_list = f.readlines()
                found = False
                for idx, info in enumerate(all_info_list):
                    if info.strip().startswith(f"{id}:"):
                        found = True
                        try:
                            course_start = info.find("'Courses':")
                            if course_start == -1:
                                print("No courses found for this student.")
                                break
                            course_end = info.find("-", course_start)
                            new_info = info[:course_start + 10] + \
                                "{}" + info[course_end:]
                            all_info_list[idx] = new_info
                            with open(file_path, "w") as f:
                                f.writelines(all_info_list)
                            print(f"All courses unregistered for ID {id}.")
                        except Exception as e:
                            print("Error processing courses:", e)
                        break
                if not found:
                    print("ID does not exist.")
        elif action == "3":
            view_option = input(
                "1-View one student\n2-View all students\n3-View all courses\n")
            if view_option == "1":
                id = input("Enter your ID number: ")
                with open(file_path, "r") as f:
                    all_info = f.read()
                    if id in all_info:
                        f.seek(0)
                        all_info_list = f.readlines()
                        print("Here is your info: ")
                        for info in all_info_list:
                            if id in info:
                                print(info)
                    else:
                        print("ID not registered.")
            elif view_option == "2":
                with open(file_path, "r") as f:
                    all_info_list = f.readlines()
                    print("All student Records:")
                    for i, info in enumerate(all_info_list):
                        print(f"{i}: {info}")
            elif view_option == "3":
                id = input("Enter your ID number: ")
                with open(file_path, "a+") as f:
                    f.seek(0)
                    all_info = f.read()
                    if id in all_info:
                        f.seek(0)
                        all_info_list = f.readlines()
                        for info in all_info_list:
                            if id in info:
                                courses_index_start = info.index("Courses")
                                courses_index_end = info.index("-")
                                print(
                                    info[courses_index_start:courses_index_end])
                    else:
                        print("ID not registered.")
        else:
            print("Please enter correct action.")
    except FileNotFoundError:
        print("File not Found, Creating new file.")
        with open(file_path, "w") as f:
            f.write("")
