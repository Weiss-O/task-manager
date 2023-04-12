import os

class Task:
    def __init__(self, title, experiencePoints, isMainQuest, isComplete):
        self.title = title
        self.experiencePoints = experiencePoints
        self.isMainQuest = isMainQuest
        self.isComplete = isComplete

mainQuests = []
sideQuests = []

# Load tasks.csv and read its contents into mainQuests array
if os.path.isfile('tasks.csv'):
    with open('tasks.csv', 'r') as f:
        for line in f:
            task_data = line.strip().split(',')
            title = task_data[0]
            experiencePoints = int(task_data[1])
            isComplete = int(task_data[2])
            mainQuests.append(Task(title, experiencePoints, True, isComplete))

# Load sideTasks.csv and read its contents into sideQuests array
if os.path.isfile('sideTasks.csv'):
    with open('sideTasks.csv', 'r') as f:
        for line in f:
            task_data = line.strip().split(',')
            title = task_data[0]
            experiencePoints = int(task_data[1])
            isComplete = int(task_data[2])
            sideQuests.append(Task(title, experiencePoints, False, isComplete))

# Print the current tasks to the console
print("Current Tasks:")
print("Main Quests:")
for task in mainQuests:
    print(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}")

print("\nSideQuests:")
for task in sideQuests:
    print(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}")

# Loop to ask user for new tasks
while True:
    add_task = input("Do you want to enter another task? (Y/N) ")
    if add_task.upper() != "Y":
        break

    # Get task details from user input
    task_name = input("What is the name of the task? ")
    task_exp_points = int(input("How many experience points? "))
    task_is_main = input("Would you consider it a main task? (Y/N) ").upper() == "Y"

    # Add task to the respective array and update the file
    if task_is_main:
        task = Task(task_name, task_exp_points, True, False)
        mainQuests.append(task)
        with open('tasks.csv', 'a') as f:
            f.write(f"{task_name},{task_exp_points},False\n")
    else:
        task = Task(task_name, task_exp_points, False, False)
        sideQuests.append(task)
        with open('sideTasks.csv', 'a') as f:
            f.write(f"{task_name},{task_exp_points},0\n")

# Print the updated tasks to the console and write them to sorted.txt
with open("sorted.txt", "w") as f:
    f.write("Main Quests:\n")
    mainQuests.sort(key=lambda task: task.experiencePoints, reverse=True)
    for task in mainQuests:
        f.write(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}\n")

    f.write("\nSideQuests:\n")
    sideQuests.sort(key=lambda task: task.experiencePoints, reverse=True)
    for task in sideQuests:
        f.write(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}\n")

print("Successfully sorted and printed to file")
