class Task:
    id = 1

    def __init__(self, description, priority):
        self.taskId = Task.id
        Task.id += 1
        self.description = description
        self.priority = priority
        self.completed = False
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, task):
        if not self.head:
            self.head = task
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = task

    def remove(self, task):
        if self.head == task:
            self.head = task.next
        else:
            current = self.head
            while current.next != None and current.next != task:
                current = current.next
            if current.next:
                current.next = current.next.next

    def getSortedTasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current)
            current = current.next
        return sorted(tasks, key=lambda task: task.priority)


class TaskManager:
    def __init__(self):
        self.taskQueue = LinkedList()
        self.taskHistory = LinkedList()

    def addTask(self, description, priority):
        task = Task(description, priority)
        self.taskQueue.append(task)

    def getTask(self, taskId):
        current = self.taskQueue.head
        while current:
            if current.taskId == taskId:
                return current
            current = current.next
        return None

    def completeHighestPriorityTask(self):
        sortedTasks = self.taskQueue.getSortedTasks()
        if sortedTasks:
            completedTask = sortedTasks[0]
            completedTask.completed = True
            self.taskQueue.remove(completedTask)
            self.taskHistory.append(completedTask)

    def displayAllTasks(self):
        tasks = self.taskQueue.getSortedTasks()
        
        for task in tasks:
            print(f"Task ID: {task.taskId}, Description: {task.description}, Priority: {task.priority}, Completed: {task.completed}")

    def displayIncompleteTasks(self):
        incompleteTasks = [task for task in self.taskQueue.getSortedTasks() if not task.completed]
        for task in incompleteTasks:
            print(f"Task ID: {task.taskId}, Description: {task.description}, Priority: {task.priority}, Completed: {task.completed}")

    def displayLastCompletedTask(self):
        tasks = self.taskHistory.getSortedTasks()
        if tasks:
            lastCompletedTask = tasks[0]
            print(f"Task ID: {lastCompletedTask.taskId}, Description: {lastCompletedTask.description}, Priority: {lastCompletedTask.priority}, Completed: {lastCompletedTask.completed}")
        else:
            print("No completed tasks in history.")


taskManager = TaskManager()

while True:
        print("Task Manager Menu:")
        print("1. Add a new task")
        print("2. Get a task by ID")
        print("3. Complete the highest priority task")
        print("4. Display all tasks in order of priority")
        print("5. Display only incomplete tasks")
        print("6. Display the last completed task")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            taskManager.addTask(description, priority)
            print("Task added successfully!")

        elif choice == '2':
            taskId = int(input("Enter task ID: "))
            task = taskManager.getTask(taskId)
            if task:
                print(f"Task found - Description: {task.description}, Priority: {task.priority}, Completed: {task.completed}")
            else:
                print("Task not found.")

        elif choice == '3':
            taskManager.completeHighestPriorityTask()
            print("Task completed and moved to history.")

        elif choice == '4':
            taskManager.displayAllTasks()

        elif choice == '5':
            taskManager.displayIncompleteTasks()

        elif choice == '6':
            taskManager.displayLastCompletedTask()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
