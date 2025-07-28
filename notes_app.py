import os
print("This is the notes app.")

if not os.path.exists("Notes"):
    os.makedirs("Notes")


def note_take():
    print("Enter your note (type 'end' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line)
    note = "\n".join(lines)
    title = input("Enter title of your note file: ").strip(
    ).title().replace(" ", "_")
    return title, note


while True:
    print("To [E]xit.")
    action = input(
        "What would you like to do:\n1-Write notes\n2-View notes\n3-Delete notes\n")
    if action.lower().strip() == "e":
        break
    if action == "1":
        write_mode_choice = input(
            "Would you like to:\n1-Make a new note\n2-Add to one\n")
        if write_mode_choice.lower().strip() == "e":
            break
        if write_mode_choice == "1":
            title, note = note_take()
            if title.lower().strip() == "e" or note.lower().strip() == "e":
                break
            if os.path.exists(f"Notes/{title}.txt"):
                print("File already exists.")
            else:
                with open(f"Notes/{title.replace(" ", "_")}.txt", "w") as f:
                    f.write(note)
                print("Note written")
        elif write_mode_choice == "2":
            title, note = note_take()
            if title.lower().strip() == "e" or note.lower().strip() == "e":
                break
            if not (os.path.exists(f"Notes/{title}")):
                print("File doesnt exist.")
            else:
                with open(f"Notes/{title.replace(" ", "_")}.txt", "a") as f:
                    f.write("\n" + note)
                print("Note written.")
        else:
            print("Please enter valid action.")
    elif action == "2":
        title = input(
            "Enter title of your note file: ").strip().title()
        if title.lower() == "e":
            break
        if not (os.path.exists(f"Notes/{title}.txt")):
            print("File doesnt exist.")
        else:
            with open(f"Notes/{title.replace(" ", "_")}.txt") as f:
                print(f.read())
    elif action == "3":
        lines_delete = []
        delete_which = input(
            "1-Delete a single line(Please remember line number)\n2-Clear whole note\n3-Delete whole file\n")
        if delete_which.lower().strip() == "e":
            break
        if delete_which == "1":
            try:
                title = input("Enter title of your note file: ").strip(
                ).title().replace(" ", "_")
                lines_to_delete = input(
                    "Please enter line(s) (Comma-seperated): ")
                if lines_to_delete.lower().strip() == "e":
                    break
                if not (os.path.exists(f"Notes/{title}.txt")):
                    print("File doesnt exist.")
                else:
                    with open(f"Notes/{title}.txt", "r") as f:
                        lines = f.readlines()
                lines_to_delete = lines_to_delete.strip().replace(" ", "").split(",")
                for line_to_delete in lines_to_delete:
                    lines_delete.append(int(line_to_delete) - 1)
                lines_delete = sorted(set(lines_delete), reverse=True)
                for line_delete in lines_delete:
                    if 0 <= line_delete < len(lines):
                        del lines[line_delete]
                with open(f"Notes/{title}.txt", "w") as f:
                    for line in lines:
                        f.write(line)
            except ValueError:
                print("Please enter a number.")
        elif delete_which == "2":
            title = input(
                "Enter title of your note file: ").strip().title().replace(" ", "_")
            if not (os.path.exists(f"Notes/{title}.txt")):
                print("File doesnt exist.")
            else:
                with open(f"Notes/{title.replace(" ", "_")}.txt", "w") as f:
                    pass
                print("File cleared.")
        elif delete_which == "3":
            title = input(
                "Enter title of your note file: ").strip().title().replace(" ", "_")
            if os.path.exists(f"Notes/{title}.txt"):
                os.remove(f"Notes/{title}.txt")
            else:
                print("File does not exist.")
        else:
            print("Please enter valid action.")
    else:
        print("Please enter valid action.")
print("Note app exited.")
