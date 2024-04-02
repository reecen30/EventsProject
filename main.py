from event_manager import EventManager

def main():
    manager = EventManager()
    while True:
        print("\n1. Add Event\n2. List Events\n3. Delete Event\n4. Search Events\n5. Edit Event\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            print(manager.add_event(title, description, date, time))
        elif choice == '2':
            print(manager.list_events())
        elif choice == '3':
            title = input("Title of event to delete: ")
            print(manager.delete_event(title))
        elif choice == '4':
            query = input("Search query: ")
            print(manager.search_events(query))
        elif choice == '5':
            original_title = input("Original title of event to edit: ")
            new_title = input("New title (optional): ")
            new_description = input("New description (optional): ")
            new_date = input("New date (YYYY-MM-DD, optional): ")
            new_time = input("New time (HH:MM, optional): ")
            print(manager.edit_event(original_title, new_title, new_description, new_date, new_time))
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
