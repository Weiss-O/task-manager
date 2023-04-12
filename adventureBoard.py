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
            print(f"{task_data[2]} {isComplete}\n")
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

# Sort the main and side quests in descending order of experience points
mainQuests.sort(key=lambda task: task.experiencePoints, reverse=True)
sideQuests.sort(key=lambda task: task.experiencePoints, reverse=True)

# Write the sorted quests to a file named sorted.txt
with open('sorted.txt', 'w') as f:
    f.write("Main Quests:\n")
    for task in mainQuests:
        f.write(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}\n")

    f.write("\nSideQuests:\n")
    for task in sideQuests:
        f.write(f"{task.title} ({task.experiencePoints} XP) - {'Complete' if task.isComplete else 'Incomplete'}\n")

print("Sorted quests written to sorted.txt")
