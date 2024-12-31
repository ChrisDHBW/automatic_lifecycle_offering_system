import os
import json
import Task

class FileHandler:

    def __init__(self):
        self.taskFilePath : str = "path-to-task-file"

    def openFile(self):
        try:
            if not os.path.exists(self.taskFilePath):
                with open(self.taskFilePath, 'w') as f:
                    json.dump([], f)  # Initialize with an empty list
            self.file = open(self.taskFilePath, 'r+')
        except Exception as e:
            print(f"Failed to open file: {e}")

    def closeFile(self):
        try:
            if self.file:
                self.file.close()
                self.file = None
        except Exception as e:
            print(f"Failed to close file: {e}")

    def saveTask(self, task : Task.Task):
        try:
            if not self.file:
                self.openFile()
            self.file.seek(0)
            tasks = json.load(self.file)
            tasks.append(task)
            self.file.seek(0)
            self.file.truncate()
            json.dump(tasks, self.file, indent=4)
        except Exception as e:
            print(f"Failed to save task: {e}")

    def updateTask(self, id : int):
        try:
            if not self.file:
                self.openFile()
            self.file.seek(0)
            tasks = json.load(self.file)
            for task in tasks:
                if task.get('id') == id:
                    break
            else:
                print(f"Task with id {id} not found.")
                return
            self.file.seek(0)
            self.file.truncate()
            json.dump(tasks, self.file, indent=4)
        except Exception as e:
            print(f"Failed to update task: {e}")

    def deleteTask(self, id : int):
        try:
            if not self.file:
                self.openFile()
            self.file.seek(0)
            tasks = json.load(self.file)
            tasks = [task for task in tasks if task.get('id') != id]
            self.file.seek(0)
            self.file.truncate()
            json.dump(tasks, self.file, indent=4)
        except Exception as e:
            print(f"Failed to delete task: {e}")
