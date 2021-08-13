"""
this program is a task manager: user can login, change login details, add tasks, read tasks
"""

#open user login details file
with open('user.txt', 'r+') as login_file:

    #set login status to false
    login = False

    #while loop while user enters login details
    while login == False:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        #concatenate username and password to be used in later conditon
        username_password = (f"{username}, {password}")

        #for loop to read the login details on file
        for line in login_file:

            #strip newline characters
            line = line.strip()

            #condition to secure username and password pair for valid login
            if username_password in line:
                login = True

        #conditional statement to display error message
        if login == False:
            print("Your details are invalid, try again!")

        #set cursor to beginning of file
        login_file.seek(0)
                 
#display menu and save selection to variable
print("")

if username == "admin":

    selection = input("""Please select one of the following options: \n
r - register user \n
a - add task \n
va - view all tasks \n
vm - view my tasks \n
st - display statistics\n
e - exit \n""")
        
else:
    print("")
    selection = input("""Please select one of the following options: \n
r - register user \n
a - add task \n
va - view all tasks \n
vm - view my tasks \n
e - exit \n""")


if selection == "r":

    #conditonal statement to ensure only 'admin' can register new users
    if username == "admin":
        
        #prompt user for new details
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        #confirm new password
        confirm_password = input("Enter the password again, to confirm: ")

        #while loop to confirm password
        while new_password != confirm_password:
            new_password = input("Enter new password: ")
            confirm_password = input("Enter the password again, to confirm: ")

        #open user file to append new user details to file
        with open('user.txt', 'a') as login_file:

            #write new user details on new line
            login_file.write("\n")
            login_file.write(f"{new_username}, {new_password}")

            #set cursor to beginning of file
            login_file.seek(0)

    elif username != "admin":
        print("You are not authorised to register a new user!")
         
elif selection == "a":
    
    #prompt for task details
    task_username = input("Who does the task belong to(username)?: ")
    task_title = input("What is the title of the task?:")
    task_description = input("Describe the task: ")
    today = input("Enter today's date (day month year): ")
    task_due = input("When is this task due? (day month year) ")
    status = "No"

    #append new details to a file
    #[user, task, description, date added, date due, complete]
    with open('tasks.txt', 'a') as task_file:

        #write new details on new line
        task_file.write("\n")
        task_file.write(f"{task_username}, {task_title}, {task_description}, {today}, {task_due}, {status}")


elif selection == "va":

    #open file in read mode
    with open('tasks.txt', 'r') as task_file:

        #read each line and split the details into seperate items
        for line in task_file:

            #save each item to variable
            task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

            #print each task group details
            print(f"""
Username:          {task_username}
Task Title:        {task_title}
Task Description:  {task_description}
Date Assigned:     {date_assigned}
Task Due Date:     {task_due}
Task Completed:    {status}
""")      

elif selection == "vm":

    #open file in read mode
    with open('tasks.txt', 'r') as task_file:

        #read each line and split the details into seperate items
        for line in task_file:

            #save each item to variable
            task_username, task_title, task_description, date_assigned, task_due, status = line.split(", ")

            #conditional statement to only display current user tasks
            if username == task_username:
                
                #print each task group details
                print(f"""
Username:          {task_username}
Task Title:        {task_title}
Task Description:  {task_description}
Date Assigned:     {date_assigned}
Task Due Date:     {task_due}
Task Completed:    {status}
""")      

elif selection == "st":

    #open user file to count users
    with open('user.txt', 'r') as user_f:

        #set number of users to 0
        num_users = 0

        #read each line, increasing the counter
        for line in user_f:
            num_users += 1

    #display number of users on file
    print(f"\nThere are {num_users} users on file.")
    
    #open task file to read lines
    with open('tasks.txt', 'r') as task_f:

        #set number of tasks to 0
        num_tasks = 0
        
        #read each line, increasing the task counter
        for line in task_f:
            num_tasks += 1

    #display number of tasks on file
    print(f"\nThere are {num_tasks} tasks on file.")

elif selection == "e":
    exit()


    
