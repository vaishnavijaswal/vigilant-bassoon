# ------------------- TO DO TASK MANAGER project(phase 1) -------------------
# NAME : VAISHNAVI JASWAL
#ENROLLMENT NO.: 2502140092


#---------- password protection ------------
password = "task123"
attempts = 3



while attempts > 0:
    entered = input("Enter password: ")
    if entered == password:
        print("Access Granted!\n")
        break
    else:
        attempts = attempts - 1
        print("Wrong password. Attempts left:", attempts)
else:
    print("Too many wrong attempts. Exiting program.")
    quit()


tasks = []
statuses = ["pending", "in-progress", "complete"]


# ---------- Function Definitions ----------
def get_new_id():
    if len(tasks) == 0:
        return 1
    else:
        last_task = tasks[-1]
        return last_task["id"] + 1



def add_task():
    tid = get_new_id()
    desc = input("Enter task description: ")
    due = input("Enter due date (YYYY-MM-DD): ")
    status = input("Enter status (pending/in-progress/complete): ")
    if status not in statuses:
        print("Invalid status, set to 'pending' by default.")
        status = "pending"
    task = {"id": tid, "description": desc, "due_date": due, "status": status}
    tasks.append(task)
    print("Task added successfully!\n")



def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nID | Description | Due Date | Status")
        print("---------------------------------------")
        for t in tasks:
            print(t["id"], "|", t["description"], "|", t["due_date"], "|", t["status"])
        print()



def modify_task():
    tid = int(input("Enter task ID to modify: "))
    found = False
    for t in tasks:
        if t["id"] == tid:
            found = True
            new_desc = input("New description (press Enter to keep same): ")
            new_due = input("New due date (press Enter to keep same): ")
            new_status = input("New status (press Enter to keep same): ")
            if new_desc != "":
                t["description"] = new_desc
            if new_due != "":
                t["due_date"] = new_due
            if new_status != "":
                if new_status in statuses:
                    t["status"] = new_status
                else:
                    print("Invalid status, keeping old one.")
            print("Task updated!\n")
            break
    if found == False:
        print("Task not found.\n")



def delete_task():
    tid = int(input("Enter task ID to delete: "))
    index = -1
    for i in range(len(tasks)):
        if tasks[i]["id"] == tid:
            index = i
            break
    if index != -1:
        del tasks[index]
        print("Task deleted!\n")
    else:
        print("Task not found.\n")



def generate_report():
    total = len(tasks)
    done = 0
    pending = 0
    progress = 0
    for t in tasks:
        if t["status"] == "complete":
            done = done + 1
        elif t["status"] == "pending":
            pending = pending + 1
        elif t["status"] == "in-progress":
            progress = progress + 1
    print("\nTotal tasks:", total)
    print("Completed:", done)
    print("In-progress:", progress)
    print("Pending:", pending, "\n")


def search_task():
    key = input("Enter keyword or status: ").lower()
    print("\nSearch Results:")
    found = False
    for t in tasks:
        if key in t["description"].lower() or key == t["status"]:
            print(t["id"], "|", t["description"], "|", t["due_date"], "|", t["status"])
            found = True
    if found == False:
        print("No matching tasks found.")
    print()

#----------- menu -----------

while True:
    print("==== TASK MANAGER ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Modify Task")
    print("4. Delete Task")
    print("5. Generate Report")
    print("6. Search Tasks")
    print("7. Exit")
    print("======================")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        modify_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        search_task()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.\n")