import csv
import os

FILE_NAME = "schedule.csv"
FIELDNAMES = ["day", "start_time", "end_time", "course_name", "location"]

def load_schedule():
    schedule = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                schedule.append(row)
    return schedule

def save_schedule(schedule):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for entry in schedule:
            writer.writerow(entry)

def add_course(schedule):
    day = input("Enter day of week (e.g., Monday): ").strip()
    start_time = input("Enter start time (HH:MM, 24h format): ").strip()
    end_time = input("Enter end time (HH:MM, 24h format): ").strip()
    course_name = input("Enter course name: ").strip()
    location = input("Enter location (room, building): ").strip()

    schedule.append({
        "day": day,
        "start_time": start_time,
        "end_time": end_time,
        "course_name": course_name,
        "location": location
    })
    save_schedule(schedule)
    print("Course added successfully.\n")

def show_schedule(schedule):
    if not schedule:
        print("No courses scheduled.\n")
        return
    print("\nFull Schedule:\n")
    print("{:<10} {:<8} {:<8} {:<20} {}".format("Day", "Start", "End", "Course", "Location"))
    print("-" * 60)
    for entry in schedule:
        print("{:<10} {:<8} {:<8} {:<20} {}".format(
            entry["day"], entry["start_time"], entry["end_time"], entry["course_name"], entry["location"]
        ))
    print()

def filter_by_day(schedule):
    day = input("Enter day to filter (e.g., Monday): ").strip()
    filtered = [entry for entry in schedule if entry["day"].lower() == day.lower()]
    if not filtered:
        print(f"No courses found for {day}.\n")
    else:
        print(f"\nSchedule for {day}:\n")
        print("{:<10} {:<8} {:<8} {:<20} {}".format("Day", "Start", "End", "Course", "Location"))
        print("-" * 60)
        for entry in filtered:
            print("{:<10} {:<8} {:<8} {:<20} {}".format(
                entry["day"], entry["start_time"], entry["end_time"], entry["course_name"], entry["location"]
            ))
        print()

def delete_course(schedule):
    show_schedule(schedule)
    try:
        index = int(input("Enter the number of the course to delete (0 to cancel): "))
        if index == 0:
            print("Deletion cancelled.\n")
            return
        if 1 <= index <= len(schedule):
            removed = schedule.pop(index - 1)
            save_schedule(schedule)
            print(f"Deleted course: {removed['course_name']} on {removed['day']}.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("=== COURSE SCHEDULE AUTOMATION SYSTEM ===")
    print("1. Add Course")
    print("2. Show Full Schedule")
    print("3. Filter Schedule by Day")
    print("4. Delete a Course")
    print("5. Exit")

def main():
    schedule = load_schedule()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        print()
        if choice == "1":
            add_course(schedule)
        elif choice == "2":
            show_schedule(schedule)
        elif choice == "3":
            filter_by_day(schedule)
        elif choice == "4":
            delete_course(schedule)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
