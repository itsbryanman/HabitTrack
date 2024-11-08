# HabitTrack
is a simple, command-line habit tracker that helps users track their daily or weekly goals, such as exercising, reading, or drinking water. It provides a visual progress chart and sends gentle reminders (if you want to get fancy). Think of it as a personal accountability buddy in script form!


Usage
Starting HabitTrack
When you run the program, you’ll see a menu with options:
Log today’s habits: Record whether you completed each habit today.
View progress: Check your streaks and overall progress.
Exit: Close the program.
Customizing Your Habits
To track different habits, open the habittrack.py file in any text editor.
Update the HABITS list near the top of the file:
python
Copy code
HABITS = ["Exercise", "Read", "Meditate"]
Replace or add any habits you want to track, such as ["Workout", "Journal", "Drink Water"].
Example Commands
Log Today’s Habits: Run the program, select “Log today’s habits,” and type y or n for each habit.

View Progress: After logging habits, choose the “View progress” option to see your streaks and a progress bar.

Data Storage
Your progress is saved in a file named habit_data.json in the project folder.
This file stores your progress history, allowing you to close and reopen the program without losing data.
Future Enhancements
Daily Reminders: Optional notifications to remind you to log habits.
Achievement Badges: Earn badges for maintaining streaks.
Web Version: Track habits via a simple web dashboard.

