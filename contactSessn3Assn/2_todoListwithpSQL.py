import psycopg2
from decouple import config



# Database connection
conn = psycopg2.connect(
    dbname="todo_db", 
    user="postgres", 
    password=config("PASSWORD"), 
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def addTodo():
    todo = input("Enter a task: ")
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (todo,))
    conn.commit()
    print(f"Task '{todo}' added to the list.")

def listTodos():
    cursor.execute("SELECT id, task FROM todos")
    rows = cursor.fetchall()
    if not rows:
        print("Nothing is in to-do list yet.")
    else:
        print("To-Do List Items:")
        for index, row in enumerate(rows, start=1):
            print(f"Task #{index}. {row[1]}")

def deleteTodo():
    listTodos()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        cursor.execute("SELECT id FROM todos ORDER BY id")
        rows = cursor.fetchall()
        if taskToDelete > 0 and taskToDelete <= len(rows):
            actual_id = rows[taskToDelete - 1][0]
            cursor.execute("DELETE FROM todos WHERE id = %s", (actual_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Task {taskToDelete} has been removed.")
            else:
                print(f"Task #{taskToDelete} was not found.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("How are you today? Start scheduling right away")
    while True:
        print("\n")
        print("Please choose an option")
        print("------------------------------------------")
        print("1. Add to todoList")
        print("2. Delete from todoList")
        print("3. List todos")
        print("4. Quit")
        print("------------------------------------------")

        choice = input("Enter your choice: ")

        print("------------------------------------------")

        if choice == "1":
            addTodo()
        elif choice == "2":
            deleteTodo()
        elif choice == "3":
            listTodos()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

    print("It's a pleasure helping your schedule, goodbye")
    cursor.close()
    conn.close()
