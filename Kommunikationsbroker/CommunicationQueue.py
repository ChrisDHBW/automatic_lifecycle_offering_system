import Task, FileHandler

class CommunicationQueue:

    def __init__(self):
        self.taskFileHandler : FileHandler.FileHandler = FileHandler.FileHandler()
        self.taskList : list[Task.Task] = []

    def addTaskToQueue(self, task : Task.Task):
        try:
            self.taskList.append(task)
            self.taskFileHandler.saveTask(task.to_dict())  # Assuming Task has a `to_dict` method
        except Exception as e:
            print(f"Failed to add task to queue: {e}")

    def updateTaskInQueue(self, index : int, newTaskData : Task.Task):
        try:
            if 0 <= index < len(self.taskList):
                self.taskList[index] = newTaskData
                self.taskFileHandler.updateTask(newTaskData.id, newTaskData.to_dict())  # Assuming Task has `id` and `to_dict`
            else:
                print(f"Invalid index: {index}. Task update failed.")
        except Exception as e:
            print(f"Failed to update task in queue: {e}")

    def removeTaskFromQueue(self, index : int):
        try:
            if 0 <= index < len(self.taskList):
                task_id = self.taskList[index].id  # Assuming Task has `id`
                del self.taskList[index]
                self.taskFileHandler.deleteTask(task_id)
            else:
                print(f"Invalid index: {index}. Task removal failed.")
        except Exception as e:
            print(f"Failed to remove task from queue: {e}")