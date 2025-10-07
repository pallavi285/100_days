tasks  = []
while True:
    print("To-Do-List")
    print("1.Add Tasks")
    print("2.Viwe Tasks")
    print("3.Mark Task as Complete")
    print("4.Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1' :
        task = input("Enter the task: ")
        tasks.append({"Task":task , "Complete": False})
        print("Task added.")
        
    elif choice == "2":
        
        if not tasks:
            print("No taks")
        else:
            print("Your task:")
            
            for i  , task_item in enumerate(tasks):
                status = "Done" if task_item["Complete"] else " "
                print(f"{i+1}.[{status}]{task_item['Task']}")
                
    elif choice == '3':
        if not tasks:
            print("No taks")
            continue 
        task_index= int(input("enter the task number:"))-1
        if 0 <= task_index < len(tasks):
            task[task_index]["Complete"] = True
            print("Task Marked as complete")
    elif choice == "4":
        print("Exiting To Do List. Goodby!")
        break
        