import csv
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
# from operator import itemgettery


# Загрузка данных
def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))



# Сообщения, присланные в ЦАП.
# id, task, variant, group, time
messages = load_csv('messages.csv')

# Результаты проверок сообщений, присланных в ЦАП.
# id, message, time, status
checks = load_csv('checks.csv')

# Состояния задач ЦАП.
# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

# Таблица соответствия номеров групп и их названий.
# id, title
groups = load_csv('groups.csv')

# 3.1
# Extract day of the week from time and count frequency
day_of_week = [parse_time(message[4]).weekday() for message in messages]
counter = Counter(day_of_week)

# Plot
plt.bar(counter.keys(), counter.values())
plt.xlabel('Day of the week')
plt.ylabel('Number of messages')
plt.title('Student activity by day of the week')
plt.show()

# 3.2
# Extract hour from time and count frequency
hour_of_day = [parse_time(message[4]).hour for message in messages]
counter = Counter(hour_of_day)

# Plot
plt.bar(counter.keys(), counter.values())
plt.xlabel('Hour of the day')
plt.ylabel('Number of messages')
plt.title('Student activity by hour of the day')
plt.show()

# 3.3
# Group messages by task and count frequency
task_messages = defaultdict(list)
for message in messages:
    task_messages[message[1]].append(message)

# Calculate average number of messages per task
average_messages = {task: len(messages) / len(task_messages) for task, messages in task_messages.items()}

# Plot
plt.bar(average_messages.keys(), average_messages.values())
plt.xlabel('Task')
plt.ylabel('Average number of messages')
plt.title('Average number of messages per task')
plt.show()

# 3.4
# Group messages by task and date, and count frequency
task_date_messages = defaultdict(list)
for message in messages:
    date = parse_time(message[4]).date()
    task_date_messages[(message[1], date)].append(message)

# Plot
for task in set(task for task, date in task_date_messages.keys()):
    dates, counts = zip(*[(date, len(messages)) for (task_, date), messages in task_date_messages.items() if task_ == task])
    plt.plot(dates, counts, label=f'Task {task}')

plt.xlabel('Date')
plt.ylabel('Number of messages')
plt.title('Student activity by task over time')
plt.legend()
plt.show()

# 3.5
# Group messages by group and count frequency
group_messages = defaultdict(list)
for message in messages:
    group_messages[message[3]].append(message)

# Plot
plt.bar(group_messages.keys(), [len(messages) for messages in group_messages.values()])
plt.xlabel('Group')
plt.ylabel('Number of messages')
plt.title('Number of messages by group')
plt.show()

# 3.6
# Group checks by group and count frequency of correct solutions
group_checks = defaultdict(list)
for check in checks:
    if check[3] == 'correct':
        group_checks[check[2]].append(check)

# Plot
plt.bar(group_checks.keys(), [len(checks) for checks in group_checks.values()])
plt.xlabel('Group')
plt.ylabel('Number of correct solutions')
plt.title('Number of correct solutions by group')
plt.show()

# 3.7
# Group checks by task and count frequency of correct solutions
task_checks = defaultdict(list)
for check in checks:
    task_checks[check[1]].append(check)

# Calculate difficulty of tasks
difficulty = {task: checks.count('incorrect') / len(checks) for task, checks in task_checks.items()}

# Plot
plt.bar(difficulty.keys(), difficulty.values())
plt.xlabel('Task')
plt.ylabel('Difficulty')
plt.title('Difficulty of tasks')
plt.show()

# 3.8
# Group statuses by group and count frequency of achievements
group_statuses = defaultdict(list)
for status in statuses:
    group_statuses[status[2]].append(status)

# Calculate total achievements per group
achievements = {group: sum(int(status[5]) for status in statuses) for group, statuses in group_statuses.items()}

# Plot
plt.bar(achievements.keys(), achievements.values())
plt.xlabel('Group')
plt.ylabel('Total achievements')
plt.title('Total achievements by group')
plt.show()
"""
# 3.9
# Group statuses by student and count frequency of correct solutions
student_statuses = defaultdict(list)
for status in statuses:
    student_statuses[status[1]].append(status)

# Calculate total correct solutions per student
correct_solutions = {student: statuses.count('correct') for student, statuses in student_statuses.items()}

# Sort students by correct solutions and take top 10
top_students = sorted(correct_solutions.items(), key=itemgetter(1), reverse=True)[:10]

# Plot
plt.bar(*zip(*top_students))
plt.xlabel('Student')
plt.ylabel('Number of correct solutions')
plt.title('Top 10 students by number of correct solutions')
plt.show()
"""
# 3.10
# Group messages by group and task, and count frequency
group_task_messages = defaultdict(list)
for message in messages:
    group_task_messages[(message[3], message[1])].append(message)

# Calculate number of unique tasks per group
unique_tasks = {group: len(set(task for group_, task in group_task_messages.keys() if group_ == group)) for group in group_messages.keys()}

# Plot
plt.bar(unique_tasks.keys(), unique_tasks.values())
plt.xlabel('Group')
plt.ylabel('Number of unique tasks')
plt.title('Number of unique tasks by group')
plt.show()