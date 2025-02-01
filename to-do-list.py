import csv

TODO_FILE = 'todo_list.csv'

# Load the to-do list from the CSV file
def load_todo_list():
    try:
        with open(TODO_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Save the to-do list to the CSV file
def save_todo_list(todo_list):
    with open(TODO_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(todo_list)

# Add new items to the to-do list
def add_items(items):
    display_todo_list()
    todo_list = load_todo_list()
    for item in items:
        todo_list.append([item, ''])
    save_todo_list(todo_list)

# Mark items as checked in the to-do list
def check_items(indices):
    display_todo_list()
    todo_list = load_todo_list()
    for index in indices:
        if 0 <= index < len(todo_list):
            todo_list[index][1] = 'x'
        else:
            print(f"Index {index} is out of range.")
    save_todo_list(todo_list)
    
# Delete items from the to-do list
def delete_items(indices):
    display_todo_list()
    todo_list = load_todo_list()
    for index in sorted(indices, reverse=True):
        if 0 <= index < len(todo_list):
            del todo_list[index]
        else:
            print(f"Index {index} is out of range.")
    save_todo_list(todo_list)

# Display the to-do list
def display_todo_list():
    print("\nTo-Do List:")
    todo_list = load_todo_list()
    for i, (item, status) in enumerate(todo_list):
        print(f"{i}. {'[x]' if status == 'x' else '[ ]'} {item}")

if __name__ == "__main__":
    print("To-Do List App")
    while True:
        print("\nOptions:")
        print("1. Add items")
        print("2. Check items")
        print("3. Delete items")
        print("4. Exit")
        choice = input("\nChoose an option: ")

        if choice == '1':
            display_todo_list()
            items = input("Enter items to add (comma separated): ").split(',')
            add_items([item.strip() for item in items])
        elif choice == '2':
            display_todo_list()
            indices = input("Enter indices to check (comma separated): ").split(',')
            check_items([int(index.strip()) for index in indices])
        elif choice == '3':
            display_todo_list()
            indices = input("Enter indices to delete (comma separated): ").split(',')
            delete_items([int(index.strip()) for index in indices])
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")
