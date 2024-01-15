import sqlite3
import datetime

# Function to create a connection to the database
def create_connection():
    return sqlite3.connect("todo_list.db")

# Function to create the tasks table
def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY,
            task_name TEXT NOT NULL,
            due_date DATE,
            status TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Function to add a new task
def add_task(task_name, due_date):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO tasks (task_name, due_date, status)
        VALUES (?, ?, 'Not Completed')
    ''', (task_name, due_date))

    connection.commit()
    connection.close()

# Function to mark a task as completed
def complete_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE tasks
        SET status = 'Completed'
        WHERE task_id = ?
    ''', (task_id,))

    connection.commit()
    connection.close()

# Function to display all tasks
def display_tasks():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM tasks
    ''')

    tasks = cursor.fetchall()

    connection.close()

    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for task in tasks:
            print("Task ID: {}, Task Name: {}, Due Date: {}, Status: {}".format(
                task[0], task[1], task[2], task[3]
            ))

# Main program
create_table()
while True:
    
    print("\nTodo List Menu:")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. Display all tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        due_date_str = input("Enter the due date (YYYY-MM-DD): ")
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
        add_task(task_name, due_date)
        print("Task added successfully!")

    elif choice == "2":
        task_id = input("Enter the task ID to mark as completed: ")
        complete_task(task_id)
        print("Task marked as completed!")

    elif choice == "3":
        display_tasks()

    elif choice == "4":
        print("Exiting Todo List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
