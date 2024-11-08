import json
from datetime import datetime

# Define a file to save progress
DATA_FILE = "habit_data.json"

# Default habits (you can add more or let users customize)
HABITS = ["Exercise", "Read", "Meditate"]

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {habit: {"streak": 0, "progress": []} for habit in HABITS}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def update_habit(data):
    today = datetime.now().strftime("%Y-%m-%d")
    for habit in HABITS:
        print(f"Did you {habit.lower()} today? (y/n)")
        response = input().strip().lower()
        if response == "y":
            if today not in data[habit]["progress"]:
                data[habit]["progress"].append(today)
                data[habit]["streak"] += 1
                print(f"Great! {habit} logged.")
            else:
                print(f"{habit} already logged for today.")
        else:
            data[habit]["streak"] = 0  # Reset streak if not done today
    save_data(data)

def show_progress(data):
    print("\n--- Habit Progress ---")
    today = datetime.now().strftime("%Y-%m-%d")
    for habit, info in data.items():
        total_days = len(info["progress"])
        streak = info["streak"]
        print(f"{habit}: {streak} day streak, {total_days} days in total.")
        progress_bar = "█" * streak + "░" * (7 - streak)
        print(f"Progress: [{progress_bar}] {streak * 100 // 7}%\n")

def main():
    data = load_data()
    while True:
        print("\nOptions:")
        print("1. Log today's habits")
        print("2. View progress")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            update_habit(data)
        elif choice == "2":
            show_progress(data)
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
